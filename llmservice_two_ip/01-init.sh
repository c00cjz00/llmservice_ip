# 注意: 請先 先編集 env.sample 內容
# Example: ./01-init.sh gpu
[[ -z "$1" ]] && { echo "Parameter 1 is empty" ; exit 1; }
IS_GPU=$1

# 目前位置
mypwd=$(pwd)

# ENV
cp env.sample .env

# DNS
rsync -av nginx_conf/ nginx

# Create Website 
rsync -av website_conf/ website

# Create Website 
rsync -av litellm_conf/ litellm

# 建立目錄
cd ${mypwd}
mkdir -p storage/anythingllm_data
mkdir -p storage/anythingllm_hotdir 
mkdir -p storage/anythingllm_outputs 
mkdir -p storage/ollama_data 
mkdir -p storage/openwebui_data 
mkdir -p storage/hf_cache 
mkdir -p storage/postgres
mkdir -p storage/pgadmin
chmod 777 storage/pgadmin
 
if ! [ -f ./storage/anythingllm_env.txt ]; then
	touch ./storage/anythingllm_env.txt
fi 

if ! [ -f ./.env ]; then
	cp ./env.sample .env
fi


# 複製compsoe file
# CPU/GPU
if [[ "$IS_GPU" == "gpu" ]] 
then
	cp compose/docker-compose_gpu.yml docker-compose.yml
else
	cp compose/docker-compose_cpu.yml docker-compose.yml
fi

# echo 
echo PORTAL: http://\$IP

