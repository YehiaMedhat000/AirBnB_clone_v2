#!/usr/bin/env bash
# Script that sets up your web servers for the deployment of web_static

# Install Nginx if it not already installed
INSTALLED=$(apt list --installed | grep -c "nginx")
if ! [ "$INSTALLED" ]; then
    sudo apt update -y
    sudo apt full-upgrade -y
    sudo apt install nginx -y
fi

# Create /data/web_static/releases/test/ if doesn't already exist
if ! [ -d /data/web_static/releases/test/ ]; then
    sudo mkdir -p /data/web_static/releases/test/
fi

# Create /data/web_static/shared/ if doesn't already exist
if ! [ -d /data/web_static/shared/ ]; then
    sudo mkdir -p /data/web_static/shared/
fi

# Create a fake HTML file /data/web_static/releases/test/index.html
if ! [ -f /data/web_static/releases/test/index.html ]; then
    echo '
<!DOCTYPE html>
<html>
<head>
    <title>NGINX Web Server Test</title>
</head>
<body style="background-color: #98FB98; text-align: center; padding-top: 50px;">
    <h1>Welcome to the NGINX Web Server Test Page</h1>
    <p>If you can see this page, it means NGINX is working correctly!</p>
    <p>Feel free to explore and customize this page further.</p>
</body>
</html>
' > index.html
    sudo mv index.html /data/web_static/releases/test/
fi

# Create the symbolic link, or recreate it
sudo ln -fs /data/web_static/releases/test /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group recursively 
sudo chown -hR ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/
# to hbnb_static
if [ -f /etc/nginx/sites-available/default ]; then
    sudo sed -i '52a\
\
        location /hbnb_static {\
                alias /data/web_static/current/;\
        }' /etc/nginx/sites-available/default
fi

# Restart nginx
sudo nginx -t
sudo service nginx restart
