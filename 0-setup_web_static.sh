#!/usr/bin/env bash
# Configuring a Web Server

# Install nginx
install_nginx() {
    # "Updating package lists..."
    sudo apt-get -y update
    # "Installing Nginx..."
    sudo apt-get -y install nginx
    # "Starting Nginx..."
    sudo service nginx restart
}

creating_data() {
    if [ ! -d /data/ ]; then
        sudo mkdir -p /data
    fi
    if [ ! -d /data/web_static/ ]; then
        sudo mkdir /data/web_static
    fi
    if [ ! -d /data/web_static/releases/ ]; then
        sudo mkdir -p /data/web_static/releases
    fi
    if [ ! -d /data/web_static/shared/ ]; then
        sudo mkdir -p /data/web_static/shared
    fi
    if [ ! -d /data/web_static/releases/test/ ]; then
        sudo mkdir -p /data/web_static/releases/test
        sudo touch  /data/web_static/releases/test/index.html
        echo "Hello this is just a test" | sudo tee /data/web_static/releases/test/index.html > /dev/null
    fi
    sudo chown -R ubuntu:ubuntu /data/
    if [ -L /data/web_static/current ]; then
        sudo rm /data/web_static/current
    fi
    sudo ln -s /data/web_static/releases/test/ /data/web_static/current

    printf %s "server {
        listen 80 default_server;
        listen [::]:80 default_server;
        root   /var/www/html;
        index  index.html index.htm;
        
        location /hbnb_static {
            alias /data/web_static/current;
            index index.html index.htm;
        }

        location /redirect_me {
            return 301 http://youtube.com/;
        }

        error_page 404 /404.html;
        location /404 {
            root /var/www/html;
            internal;
        }
    }" > /etc/nginx/sites-available/default
}

# Checking if nginx is installed or not
if nginx -v >/dev/null 2>&1; then
    # "Nginx is Installed"
    creating_data
else
    install_nginx
    creating_data
fi
sudo service nginx restart
