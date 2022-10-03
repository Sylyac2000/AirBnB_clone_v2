#!/usr/bin/env bash
#install nginx and create some Folders

install_nginx(){
	apt-get  update -y &> /dev/null
	apt-get  upgrade -y &> /dev/null
	apt-get  install nginx -y &> /dev/null
}
create_folders(){
	mkdir -p /data/
	mkdir -p /data/web_static/
	mkdir -p /data/web_static/releases/
	mkdir -p /data/web_static/shared/
	mkdir -p /data/web_static/releases/test/
}

create_index(){
	echo "Salam ALX" | sudo tee /data/web_static/releases/test/index.html >/dev/null
}

create_symbolic(){
	#create simbolic link(ln-s cible destination_ou_nom)
	sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
}

change_owner(){
	#Give ownership of the /data/ folder to ubuntu:ubuntu recursive
	sudo chown -hRf ubuntu:ubuntu /data/*
}

update_nginx_default() {
	#Update the Nginx configuration
	sudo sed -i '63i\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
}
main() {

	install_nginx
	create_folders
	create_index
	create_symbolic
	change_owner
	update_nginx_default

}
main

sudo service nginx restart
