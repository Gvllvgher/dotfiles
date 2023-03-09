from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from modules.keys import terminal, alt_terminal
from modules.colors import palette
from modules.desktop import desktop_screens
from modules.notebook import notebook_screen
import os
import re
import subprocess

machine_info = subprocess.check_output(["hostnamectl", "status"], universal_newlines=True)
m = re.search('Chassis: (.+?)\n', machine_info)
chassis_type = m.group(1)

if 'laptop' in chassis_type:
    screens = notebook_screen
else:
    screens = desktop_screens
