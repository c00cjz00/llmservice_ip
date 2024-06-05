# 切換目錄
cd ~/llmservice_dns/llmservice_one_dns/

# 關閉服務
docker compose down

# 刪除anythingllm相關資料
rm -rf storage/anythingllm_*


# 重建anythingllm相關資料
mkdir -p storage/anythingllm_data
mkdir -p storage/anythingllm_hotdir
mkdir -p storage/anythingllm_outputs
touch ./storage/anythingllm_env.txt

# 啟動服務
docker compose up -d

# 打開網頁
https://anythingllm2ntuh.biobank.org.tw 





