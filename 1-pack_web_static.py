#!/usr/bin/python3
"""
 a Fabric script that generates a .tgz
 archive from the contents of the web_static folder
 of your AirBnB Clone repo
"""
from fabric.api import local
from time import strftime


def do_pack():
    """generate .tgz archive of web_static/ folder"""
    thetime = strftime("%Y%M%d%H%M%S")
    try:
        local("mkdir -p versions")
        filename = "versions/web_static_{}.tgz".format(thetime)
        local("tar -cvzf {} web_static/".format(filename))
        return filename
    except:
        return None
