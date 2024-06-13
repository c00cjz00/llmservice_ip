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
mkdir -p storage/factory_data storage/factory_saves storage/factory_cache storage/jupyter_data
mkdir -p storage/output
mkdir -p storage/mergekit_tmp
mkdir -p storage/qdrant_data
cp factory_conf/data/dataset_info.json storage/factory_data/
cp factory_conf/data/identity.json storage/factory_data/
cp factory_conf/data/alpaca_en_demo.json storage/factory_data/
cp factory_conf/data/c4_demo.json storage/factory_data/
rsync -avHS factory/ factory
rsync -avHS factory_conf/examples/ storage/factory_examples
rsync -avHS notebook_conf/ storage/jupyter_data/notebook
rsync -avHS mergekit_conf/ mergekit

 
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

