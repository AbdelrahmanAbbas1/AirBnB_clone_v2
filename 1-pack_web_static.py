#!/usr/bin/python3
"""This module define a Fabric script to generate a .tgz archive"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Genertaes a .tgz archive and returns the archive path"""
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    new_archive = "web_static_{}.tgz".format(date)
    new_archive_path = "versions/{}".format(new_archive)
    gzip_result = local("tar -czvf {} web_static".format(new_archive_path))
    if gzip_result.succeeded:
        return new_archive_path
    else:
        return None
