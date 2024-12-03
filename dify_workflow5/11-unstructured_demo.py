## singularity pull docker://downloads.unstructured.io/unstructured-io/unstructured:latest
## singularity exec -B /work unstructured_latest.sif bash -c "export PYTHONPATH=/home/notebook-user/.local/lib/python3.11/site-packages:/app; python3 unstructured_demo.py"
## 請先點選工作列 [執行階段]-> 重新啟動工作階段
## 請先點選工作列 [編輯]-> 清除所有輸出內容
## 右側RAM/磁碟標記 -> 變更執行階段 -> T4 GPU
# Read PDF
from typing import Any
from pydantic import BaseModel
from unstructured.partition.pdf import partition_pdf
#from unstructured.partition.auto import partition
# 使用 unstructured.io 解析中文文本
#elements = partition(file=file_io, languages=["chi_sim"])

#1
raw_pdf_elements = partition_pdf(
    filename="./1Q23-EPR-with-Tables-FINAL.pdf",
    languages=["chi_tra", "chi_tra_vert","chi_sim", "chi_sim_vert"],
    #languages=["chi_tra", "chi_tra_vert","chi_sim", "chi_sim_vert"])
    extract_images_in_pdf=False,
    infer_table_structure=True,
    #include_page_breaks=True,
    chunking_strategy="by_title",
    max_characters=4000,
    new_after_n_chars=3800,
    combine_text_under_n_chars=2000,
    image_output_dir_path="./im2",
)

#2
category_counts = {}

for element in raw_pdf_elements:
    category = str(type(element))
    if category in category_counts:
        category_counts[category] += 1
    else:
        category_counts[category] = 1

unique_categories = set(category_counts.keys())
category_counts

#3
class Element(BaseModel):
    type: str
    text: Any

table_elements = []
text_elements = []
all_elements = []
for element in raw_pdf_elements:
    if "unstructured.documents.elements.Table" in str(type(element)):
        text=str(element)
        text = ''.join(text.split())
        table_elements.append(Element(type="table", text=text))
        all_elements.append(Element(type="table", text=text))
    elif "unstructured.documents.elements.CompositeElement" in str(type(element)):
        text=str(element)
        text = ''.join(text.split())
        text_elements.append(Element(type="text", text=text))
        all_elements.append(Element(type="text", text=text))

#4
#print(len(table_elements))
#print(len(text_elements))
#print(len(all_elements))

for i, all in enumerate(all_elements):
    print('cutoff', i, all)

