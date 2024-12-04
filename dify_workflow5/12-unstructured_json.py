## singularity pull docker://downloads.unstructured.io/unstructured-io/unstructured:latest
## time singularity exec -B /work unstructured_latest.sif bash -c "export PYTHONPATH=/home/notebook-user/.local/lib/python3.11/site-packages:/app; python3 12-unstructured_json.py ./1Q23-EPR-with-Tables-FINAL.pdf"
## 輸出 ./1Q23-EPR-with-Tables-FINAL.pdf.json
# Read PDF
import sys
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('no argument')
        sys.exit()
    
    pdf_file = sys.argv[1]
    
from typing import Any
from pydantic import BaseModel
from unstructured.partition.pdf import partition_pdf
#from unstructured.partition.auto import partition

#1
raw_pdf_elements = partition_pdf(
    #filename="./1Q23-EPR-with-Tables-FINAL.pdf",
    filename=pdf_file,
    languages=["chi_tra", "chi_tra_vert","chi_sim", "chi_sim_vert"],
    #languages=["chi_tra", "chi_tra_vert","chi_sim", "chi_sim_vert"])
    extract_images_in_pdf=False,
    infer_table_structure=True,
    #include_page_breaks=True,
    chunking_strategy="by_title",
    max_characters=4000,
    new_after_n_chars=3800,
    combine_text_under_n_chars=2000,
    image_output_dir_path="./img",
)

# get output as json
from unstructured.staging.base import elements_to_json
json_filename=pdf_file+".json"
elements_to_json(raw_pdf_elements, filename=json_filename)
