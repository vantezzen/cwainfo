"""
CWAInfo CWA BLE Debugging
Constantly log number of device in proximity
~~~~~~~~~~~~~~~~~~~
:copyright: (c) 2021-present Bennett Hollstein
:license: MIT, see LICENSE for more details.
"""
import os
import configparser
from collector import Collector


project_dir = os.path.dirname(__file__)
if len(project_dir) != 0:
    project_dir += "/"

config = configparser.ConfigParser()
config.read('config.ini')

collector = Collector()
collected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while True:
  devices = collector.scan()
  collected[devices] += 1;
  print(collected)
