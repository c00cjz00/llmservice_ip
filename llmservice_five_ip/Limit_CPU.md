https://blog.yowko.com/docker-compose-3-cpu-memory-limit/

https://stackoverflow.com/questions/48685667/what-does-docker-mean-when-it-says-memory-limited-without-swap

https://charlie-c.medium.com/%E7%94%A8docker%E5%BB%BA%E7%AB%8Bphp-nginx-%E9%96%8B%E7%99%BC%E7%92%B0%E5%A2%83-33c5f88edeb3

為了解決上述問題，請使用下列項目更新 grub 檔案：

fgrep GRUB_CMDLINE_LINUX /etc/default/grub
GRUB_CMDLINE_LINUX_DEFAULT="maybe-ubiquity"
GRUB_CMDLINE_LINUX="cgroup_enable=memory swapaccount=1"
現在更新 grub：

root@ubuntuserver:~# update-grub
Sourcing file `/etc/default/grub'
Generating grub configuration file ...
Found linux image: /boot/vmlinuz-4.15.0-74-generic
Found initrd image: /boot/initrd.img-4.15.0-74-generic
done
root@ubuntuserver:~#
完成後重新啟動機器並建立具有記憶體限制的容器：

root@ubuntuserver:~# docker container run -d -ti --hostname testcontainer -- 
name testubuntu2 --restart=always --memory="50m" --memory-swap=0 --cpus="0.5" 
ubuntu:16.04
93969354be0445f3458999259747d82231b4084728c3ccf8801dc89be8aadaa3
root@ubuntuserver:~#
