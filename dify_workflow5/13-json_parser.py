## singularity pull docker://downloads.unstructured.io/unstructured-io/unstructured:latest
## time singularity exec -B /work unstructured_latest.sif bash -c "export PYTHONPATH=/home/notebook-user/.local/lib/python3.11/site-packages:/app; python3 13-json_parser.py ./1Q23-EPR-with-Tables-FINAL.pdf.json"
#
import sys
import pandas as pd
import json

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('no argument')
        sys.exit()
    json_file=sys.argv[1]
    data = pd.read_json ( json_file )
    df = pd.DataFrame(data) # 轉成 DataFrame
    for index, row in df.iterrows():
        type=row['type']
        #if type == "Table":
        #print(index)
        print('cutoff', '"filename":"'+row['metadata']['filename']+'",', '"index":'+str(index), '"page_number":'+str(row['metadata']['page_number'])+',',  '"type":"'+row['type']+'"',  '"text":"'+repr(row['text'])+'"')
            