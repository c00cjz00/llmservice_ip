# nchc service

## DOCKER 安裝
- https://hackmd.io/@whYPD8MBSHWRZV6y-ymFwQ/Hk8pJ95eA
- https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html

## 更新套件
```
sudo apt update
sudo apt install php7.4-cli jq
```

## GIT 下載套件
```
git clone https://github.com/c00cjz00/llmservice_ip.git
cd llmservice_ip/llmservice_litellm_dns
```

## 編輯env.sample
```
vi  env.sample 
```

## 確認您的IP以及是否有GPU, 並執行以下指令
- ./01-init.sh [cpu/gpu]
```
./01-init.sh
``` 

## 啟動服務
- activate
```
docker compose up -d && docker restart nchc_litellm
```
- check 
```
docker logs -f nchc_litellm
```
- if nchc_litellm not work
```
docker restart nchc_litellm

```

## 關閉服務
```
docker compose down 
```

## 服務網址 
- litell api: http://$IP:4000
- litell ui: http://$IP:4000/ui/
- postgres api: http://$IP:5432
- pgadmin4 api: http://$IP:5080
- portal: http://$IP:80

## 內部服務器
- litell api: http://host.docker.internal:4000
- postgres api: http://host.docker.internal:5432

