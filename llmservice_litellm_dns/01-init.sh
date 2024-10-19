# 注意: 請先 先編集 env.sample 內容
# Example: ./01-init.sh

# 目前位置
mypwd=$(pwd)

# 建立目錄
cd ${mypwd}
mkdir -p storage/postgres
mkdir -p storage/pgadmin
chmod 777 storage/pgadmin
 
# ENV
if ! [ -f ./.env ]; then
	cp ./env.sample .env
fi


