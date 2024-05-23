#!/usr/bin/env bash
# Configuring a Web Server

# Install nginx
install_nginx() {
    echo "Updating package lists..."
    sudo apt-get -y update
    echo "Installing Nginx..."
    sudo apt-get -y install nginx
    echo "Starting Nginx..."
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
        echo "Hello this is just a test" | sudo tee /data/web_static/releases/test/index.html
    fi
    sudo chown -R ubuntu:ubuntu /data/
    if [ -L /data/web_static/current ]; then
        sudo rm /data/web_static/current
    fi
    sudo ln -s /data/web_static/releases/test/ /data/web_static/current
    
    sudo sed -i "59i\
    \tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tindex index.html index.htm\n\t}" /etc/nginx/sites-available/default
}

# Checking if nginx is installed or not
if nginx -v >/dev/null 2>&1; then
    echo "Nginx is Installed"
    creating_data
else
    install_nginx
    creating_data
fi
sudo service nginx restart
