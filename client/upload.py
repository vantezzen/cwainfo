"""
CWAInfo
Only upload
~~~~~~~~~~~~~~~~~~~
:copyright: (c) 2021-present Bennett Hollstein
:license: MIT, see LICENSE for more details.
"""
import os
import configparser
from uploader import Uploader

project_dir = os.path.dirname(__file__)
if len(project_dir) != 0:
    project_dir += "/"

config = configparser.ConfigParser()
config.read('config.ini')

uploader = Uploader()
uploader.upload(config)
