#!/usr/bin/python3
"""Fabric script that creates and distributes an archive to web servers"""
import os
from fabric.api import *
do_pack = __import__("1-pack_web_static").do_pack
do_deploy = __import__("2-do_deploy_web_static").do_deploy

# Variable to keep track of the function calls
archive = None


def deploy():
    """This function depolys an archive to servers"""
    global archive
    # Ensure do_pack is called only once
    if archive is None:
        archive = do_pack()
        if archive is None:
            return False
    # Store the archive created by do_pack because it will be only called once
    archive_path = archive
    res = do_deploy(archive_path)
    return res
