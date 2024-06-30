from libqtile.config import Key, Group, ScratchPad, DropDown
from libqtile.lazy import lazy
from .keys import keys, mod, terminal

groups = [
    Group(name="1", label=" "),
    Group(name="2", label=" "),
    Group(name="3", label=" "),
    Group(name="4", label=" "),
    Group(name="5", label=" "),
    Group(name="6", label=" "),
    Group(name="7", label=" "),
    Group(name="8", label="󰇰 "),
    Group(name="9", label=" "),
    ScratchPad("0", [DropDown("term", terminal, opacity=0.9, height=0.6, width=0.80)])
]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod],
            i.name,
            lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"],
            i.name,
            lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])
