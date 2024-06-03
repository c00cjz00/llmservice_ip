import os
import pathlib
import random
import string
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor
from typing import Iterable, List

import gradio as gr
import huggingface_hub
import torch
import yaml
from gradio_logsview.logsview import Log, LogsView, LogsViewRunner
from mergekit.config import MergeConfiguration

from clean_community_org import garbage_collect_empty_models

has_gpu = torch.cuda.is_available()

# Running directly from Python doesn't work well with Gradio+run_process because of:
# Cannot re-initialize CUDA in forked subprocess. To use CUDA with multiprocessing, you must use the 'spawn' start method
# Let's use the CLI instead.
#
# import mergekit.merge
# from mergekit.common import parse_kmb
# from mergekit.options import MergeOptions
#
# merge_options = (
#     MergeOptions(
#         copy_tokenizer=True,
#         cuda=True,
#         low_cpu_memory=True,
#         write_model_card=True,
#     )
#     if has_gpu
#     else MergeOptions(
#         allow_crimes=True,
#         out_shard_size=parse_kmb("1B"),
#         lazy_unpickle=True,
#         write_model_card=True,
#     )
# )

cli = "mergekit-yaml config.yaml merge --copy-tokenizer" + (
    " --cuda --low-cpu-memory --allow-crimes" if has_gpu else " --allow-crimes --out-shard-size 1B --lazy-unpickle"
)

MARKDOWN_DESCRIPTION = """
# 混合模型服務平台

The fastest way to perform a model merge 🔥

Specify a YAML configuration file (see examples below) and a HF token and this app will perform the merge and upload the merged model to your user profile.
"""

MARKDOWN_ARTICLE = """
___

"""

examples = [[str(f)] for f in pathlib.Path("examples").glob("*.yaml")]

# Do not set community token as `HF_TOKEN` to avoid accidentally using it in merge scripts.
# `COMMUNITY_HF_TOKEN` is used to upload models to the community organization (https://huggingface.co/mergekit-community)
# when user do not provide a token.
COMMUNITY_HF_TOKEN = os.getenv("COMMUNITY_HF_TOKEN")


def merge(yaml_config: str, hf_token: str, repo_name: str) -> Iterable[List[Log]]:
    runner = LogsViewRunner()

    if not yaml_config:
        yield runner.log("Empty yaml, pick an example below", level="ERROR")
        return
    try:
        merge_config = MergeConfiguration.model_validate(yaml.safe_load(yaml_config))
    except Exception as e:
        yield runner.log(f"Invalid yaml {e}", level="ERROR")
        return

    is_community_model = False
    if not hf_token:
        if "/" in repo_name and not repo_name.startswith("mergekit-community/"):
            yield runner.log(
                f"Cannot upload merge model to namespace {repo_name.split('/')[0]}: you must provide a valid token.",
                level="ERROR",
            )
            return
        yield runner.log(
            "No HF token provided. Your merged model will be uploaded to the https://huggingface.co/mergekit-community organization."
        )
        is_community_model = True
        if not COMMUNITY_HF_TOKEN:
            raise gr.Error("Cannot upload to community org: community token not set by Space owner.")
        hf_token = COMMUNITY_HF_TOKEN

    api = huggingface_hub.HfApi(token=hf_token)

    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmpdirname:
        tmpdir = pathlib.Path(tmpdirname)
        merged_path = tmpdir / "merged"
        merged_path.mkdir(parents=True, exist_ok=True)
        config_path = merged_path / "config.yaml"
        config_path.write_text(yaml_config)
        yield runner.log(f"Merge configuration saved in {config_path}")

        if not repo_name:
            yield runner.log("No repo name provided. Generating a random one.")
            repo_name = f"mergekit-{merge_config.merge_method}"
            # Make repo_name "unique" (no need to be extra careful on uniqueness)
            repo_name += "-" + "".join(random.choices(string.ascii_lowercase, k=7))
            repo_name = repo_name.replace("/", "-").strip("-")

        if is_community_model and not repo_name.startswith("mergekit-community/"):
            repo_name = f"mergekit-community/{repo_name}"

        try:
            yield runner.log(f"Creating repo {repo_name}")
            repo_url = api.create_repo(repo_name, exist_ok=True)
            yield runner.log(f"Repo created: {repo_url}")
        except Exception as e:
            yield runner.log(f"Error creating repo {e}", level="ERROR")
            return

        # Set tmp HF_HOME to avoid filling up disk Space
        tmp_env = os.environ.copy()  # taken from https://stackoverflow.com/a/4453495
        tmp_env["HF_HOME"] = f"{tmpdirname}/.cache"
        full_cli = cli + f" --lora-merge-cache {tmpdirname}/.lora_cache"
        yield from runner.run_command(full_cli.split(), cwd=merged_path, env=tmp_env)

        if runner.exit_code != 0:
            yield runner.log("Merge failed. Deleting repo as no model is uploaded.", level="ERROR")
            api.delete_repo(repo_url.repo_id)
            return

        yield runner.log("Model merged successfully. Uploading to HF.")
        yield from runner.run_python(
            api.upload_folder,
            repo_id=repo_url.repo_id,
            folder_path=merged_path / "merge",
        )
        yield runner.log(f"Model successfully uploaded to HF: {repo_url.repo_id}")


with gr.Blocks() as demo:
    gr.Markdown(MARKDOWN_DESCRIPTION)

    with gr.Row():
        filename = gr.Textbox(visible=False, label="filename")
        config = gr.Code(language="yaml", lines=10, label="config.yaml")
        with gr.Column():
            token = gr.Textbox(
                lines=1,
                label="HF Write Token",
                info="https://hf.co/settings/token",
                type="password",
                placeholder="Optional. Will upload merged model to MergeKit Community if empty.",
            )
            repo_name = gr.Textbox(
                lines=1,
                label="Repo name",
                placeholder="Optional. Will create a random name if empty.",
            )
    button = gr.Button("Merge", variant="primary")
    logs = LogsView(label="Terminal output")
    gr.Examples(
        examples,
        fn=lambda s: (s,),
        run_on_click=True,
        label="Examples",
        inputs=[filename],
        outputs=[config],
    )
    gr.Markdown(MARKDOWN_ARTICLE)

    button.click(fn=merge, inputs=[config, token, repo_name], outputs=[logs])


# Run garbage collection every hour to keep the community org clean.
# Empty models might exists if the merge fails abruptly (e.g. if user leaves the Space).
def _garbage_collect_every_hour():
    while True:
        try:
            garbage_collect_empty_models(token=COMMUNITY_HF_TOKEN)
        except Exception as e:
            print("Error running garbage collection", e)
        time.sleep(3600)


pool = ThreadPoolExecutor()
pool.submit(_garbage_collect_every_hour)


server_name = os.environ.get("GRADIO_SERVER_NAME", "0.0.0.0")
server_port = int(os.environ.get("GRADIO_SERVER_PORT", "8860"))
gradio_share = bool(int(os.environ.get("GRADIO_SHARE", "0")))
gradio_user = os.environ.get("GRADIO_USER", "nchc")
gradio_password = os.environ.get("GRADIO_PASSWORD", "nchcorgtw")    
#demo.queue(default_concurrency_limit=1).launch()
demo.queue(default_concurrency_limit=1).launch(share=gradio_share, server_name=server_name, server_port=server_port,auth=(gradio_user, gradio_password))
