#!/usr/bin/python3
"""Fabric script that ditributes an archive to web servers"""
import os
from fabric.api import *

env.hosts = ['100.25.181.194', '54.237.49.41']


def do_deploy(archive_path):
    """ This function deploy an archive to web servers"""
    if os.path.exists(archive_path) is False:
        return False

    folder = archive_path.split("/")[-1]
    name = folder.split(".")[0]

    if put(archive_path, "/tmp/").succeeded is False:
        return False
    if run("sudo mkdir -p /data/web_static/releases/{}".
           format(name)).succeeded is False:
        return False
    if run("sudo tar -xzvf /tmp/{} -C /data/web_static/releases/{}/".
           format(folder, name)).succeeded is False:
        return False
    if run("sudo rm -f /tmp/{}".format(folder)).succeeded is False:
        return False
    if run("sudo rm -rf /data/web_static/current").succeeded is False:
        return False
    if run("sudo ln -s /data/web_static/releases/{} /data/web_static/current".
           format(name)).succeeded is False:
        return False
    return True
