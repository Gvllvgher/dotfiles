from libqtile import layout
from libqtile.config import Match
from modules.colors import palette

layouts = [
    layout.Bsp(
        grow_amount = 2,
        border_on_single = False,
        margin = 10,
        border_focus = palette["light_border"],
        border_normal = palette["dark_border"],
        border_width = 1
    )
]

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),
    Match(wm_class='makebranch'),
    Match(wm_class='maketag'),
    Match(wm_class='Alacritty'),
    Match(wm_class='flameshot'),
    Match(wm_class='xfce4-power-manager-settings'),
    Match(wm_class='ssh-askpass'),
    Match(title='branchdialog'),
    Match(title='pinentry'),
])
