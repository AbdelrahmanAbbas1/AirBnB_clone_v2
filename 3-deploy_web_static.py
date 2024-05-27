#!/usr/bin/python3
"""Fabric script that creates and distributes an archive to web servers"""
import os
from fabric.api import *
do_pack = __import__("1-pack_web_static").do_pack
do_deploy = __import__("2-do_deploy_web_static").do_deploy

env.hosts = ["100.25.181.194", "54.237.49.41"]


def deploy():
    """This function depolys an archive to servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    res = do_deploy(archive_path)
    return res
