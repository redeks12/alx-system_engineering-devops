# Automating project requirements using Puppet

exec { add_header:
    command =>"sudo apt-get update
    sudo apt-get -y install nginx
    sudo ufw allow 'Nginx HTTP'
    sudo sed -i 's|server_name _;|server_name _;\n\tadd_header X-Served-By $HOSTNAME;|' /etc/nginx/sites-enabled/default
    sudo nginx -t
    sudo service nginx restart",

    provider => "shell"

}