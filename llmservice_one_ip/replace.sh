#sed -i 's/${IP}/$1/g' website/index_ds_ip.html
#sed -i 's/$1/203.145.221.169/g' website/index_ds_ip.html
sed -i 's/${IP}/203.145.221.164/g' website/index_factory_ip.html

sed -i 's$/usr/share/nginx/html$/var/www/html$g' *conf

# 
