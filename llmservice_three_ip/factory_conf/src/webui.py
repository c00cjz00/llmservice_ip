import os

from llmtuner.webui.interface import create_ui


def main():
    server_name = os.environ.get("GRADIO_SERVER_NAME", "0.0.0.0")
    server_port = int(os.environ.get("GRADIO_SERVER_PORT", "7860"))
    gradio_share = os.environ.get("GRADIO_SHARE", "0").lower() in ["true", "1"]
    gradio_user = os.environ.get("GRADIO_USER", "nchc")
    gradio_password = os.environ.get("GRADIO_PASSWORD", "nchcorgtw")    
    #create_ui().queue().launch(share=gradio_share, server_name=server_name, server_port=server_port)
    create_ui().queue().launch(share=gradio_share, server_name=server_name, server_port=server_port,auth=(gradio_user, gradio_password))


if __name__ == "__main__":
    main()

