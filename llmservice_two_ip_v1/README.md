# nchc service

## 初始設定
1. DOCKER 安裝
請參考以下連結
https://hackmd.io/@whYPD8MBSHWRZV6y-ymFwQ/r1Wbg9DrA 

2. 更新套件
```
sudo apt update
sudo apt install php7.4-cli jq
```

## Step 1: GIT 下載套件
```
git clone https://github.com/c00cjz00/llmservice_ip.git
cd llmservice_ip/llmservice_two_ip_v1
```

## Step 2: 編輯env.sample
```
vi  env.sample 
```

## Step3: 確認您的IP以及是否有GPU, 並執行以下指令
- ./01-init.sh [cpu/gpu]
```
./01-init.sh gpu
``` 

## Step 4: 啟動服務
- activate
```
docker compose up -d 
```
- check nchc_litellm
```
docker logs -f nchc_litellm
```
- if nchc_litellm not work
```
docker restart nchc_litellm

```

## Step 5: 關閉服務
```
docker compose down 
```

## Step 6: 服務網址 
- openwebui: http://$IP:8080
- ollama api: http://$IP:11434
- anythingllm: http://$IP:3001
- litell api: http://$IP:4000
- litell ui: http://$IP:4000/ui/
- postgres api: http://$IP:5432
- pgadmin4 api: http://$IP:5080
- portal: http://$IP:80

## Step 7: 內部服務器
- ollama api: http://host.docker.internal:11434
- litell api: http://host.docker.internal:4000
- postgres api: http://host.docker.internal:5432

## 注意事項: Ollama Template, 記憶體太小請修正 num_ctx=2048
```
FROM ./taide-8b-a.3-q4_k_m.gguf
TEMPLATE """{{ if .System }}<|start_header_id|>system<|end_header_id|>

{{ .System }}<|eot_id|>{{ end }}{{ if .Prompt }}<|start_header_id|>user<|end_header_id|>

{{ .Prompt }}<|eot_id|>{{ end }}<|start_header_id|>assistant<|end_header_id|>

{{ .Response }}<|eot_id|>"""
PARAMETER stop "<|start_header_id|>"
PARAMETER stop "<|end_header_id|>"
PARAMETER stop "<|eot_id|>"
PARAMETER num_keep 24
PARAMETER num_ctx 4096
```

## 注意事項:  GPU
```
sudo nvidia-smi -pm 1
sudo nvidia-smi -e 0
```
