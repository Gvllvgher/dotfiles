from libqtile import bar
from modules.widgets import *
from libqtile.config import Screen
from modules.colors import palette
import re
import subprocess

machine_info = subprocess.check_output(["hostnamectl", "status"], universal_newlines=True)
m = re.search('Chassis: (.+?)\n', machine_info)
assert m is not None
chassis_type = m.group(1)

if 'laptop' in chassis_type:
    widgets = [
        separator,
        groupbox,
        separator_large,
        widget.Prompt(),
        widget.Spacer(length=5),
        windowname,
        widget.Spacer(),
        clock,
        widget.Spacer(),
        chord,
        checkupdates,
        systray,
        separator,
        line,
        volume, 
        separator_medium,
        backlight_icon,
        backlight,
        separator_medium,
        bluetooth,
        separator_medium,
        line,
        openweather,
        line,
        processor,
        line,
        memory,
        line,
        battery,
        separator_large,
        power,
        widget.Spacer(length=5),
        separator_large
    ]
else:
    widgets = [   
        separator,
        groupbox,
        separator,
        widget.Prompt(),
        widget.Spacer(length=5),
        windowname,
        widget.Spacer(),
        clock,
        widget.Spacer(),
        chord,
        currentlayout,
        checkupdates,
        systray,
        separator_medium,
        volume, 
        separator_medium,
        separator_medium,
        bluetooth,
        separator_medium,
        line,
        openweather,
        line,
        processor,
        line,
        memory,
        line,
        network,
        line,
        separator_large,
        power,
        widget.Spacer(length=5),
        separator_large
    ]

screens = [
    Screen(
        top=bar.Bar(
            widgets,
            32,  # height in px
            background=palette["dark_background"],  # background color
            opacity=0.9, # Was 0.8
            margin=[
                10,
                10,
                2,
                10
            ]
        ),
    ),
]
