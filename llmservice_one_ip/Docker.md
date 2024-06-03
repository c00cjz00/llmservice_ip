# NVIDIA DRIVER AND INSTALL DOCKER
## 1. 安裝 NIVIDA 驅動程式
```
# 更新系統
sudo apt update && sudo apt upgrade -y
# 移除所有nvidia套件
sudo apt autoremove nvidia* --purge -y
# 安裝ubuntu nvudia 套件
sudo apt install ubuntu-drivers-common -y
# 列出nvidia可安裝DRIVER版本
ubuntu-drivers devices
ubuntu-drivers list
# 並動更新, 若移除以下第二行之# 指定版本
sudo ubuntu-drivers autoinstall
#sudo apt install nvidia-driver-525
# 列出顯卡硬體內容
sudo lshw -C display
# 重開機
sudo reboot now

```

## 2. 安裝 Docker
- 移除
```
sudo apt-get remove docker docker-engine docker.io containerd runc
sudo apt-get update
docker volume ls -q -f driver=nvidia-docker | xargs -r -I{} -n1
docker ps -q -a -f volume={} | xargs -r docker rm -f
sudo apt-get purge -y nvidia-docker
```

- 安裝 docker-ce
```
sudo apt-get update -y
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
sudo apt-get update -y
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y
```

- 安裝NVIDIA Container Toolkit (nvidia-docker2)
```
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
sudo apt-get update -y
sudo apt-get install nvidia-docker2 -y
sudo systemctl restart docker.service

sudo systemctl restart docker

```
- 測試是否成功
```
sudo docker run --rm --gpus all nvidia/cuda:11.6.2-base-ubuntu20.04 nvidia-smi
```


- 加入 Docker 群組, 記得你的身分為ubuntu
```
sudo groupadd docker
sudo usermod -aG docker $USER
sudo systemctl enable docker  # 啟動 Docker 服務
docker --version
```

- 測試安裝結果, 記得你的身分為ubuntu
```
sudo su 
su ubuntu
docker run hello-world
```
