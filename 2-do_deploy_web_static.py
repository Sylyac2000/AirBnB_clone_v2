#!/usr/bin/python3
"""
Fabric script to deploys archive to webservers
Usage:
    fab -f 2-do_deploy_web_static.py
    do_deploy:archive_path=versions/web_static_20224802224837.tgz
    -i my_ssh_private_key -u ubuntu
"""
from fabric.api import env, put, run
import os.path
env.hosts = ['3.238.247.215', '35.173.50.224']
env.identity = '~/.ssh/id_rsa'
env.user = 'ubuntu'
env.password = None

def do_deploy(archive_path):
    """
    Deploy archive to web server
    """
    if os.path.isfile(archive_path) is False:
        return False
    try:
        thefilename = archive_path.split("/")[-1]
        no_extension = thefilename.split(".")[0]
        path_no_exten = "/data/web_static/releases/{}/".format(no_exten)
        symbolic_link = "/data/web_static/current"
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(path_no_exten))
        run("tar -xzf /tmp/{} -C {}".format(thefilename, path_no_exten))
        #run("rm /tmp/{}".format(thefilename))
        run("mv {}web_static/* {}".format(path_no_exten, path_no_exten))
        run("rm -rf {}web_static".format(path_no_exten))
        run("rm -rf {}".format(symbolic_link))
        run("ln -s {} {}".format(path_no_exten, symbolic_link))
        return True
    except Exception:
        return False
