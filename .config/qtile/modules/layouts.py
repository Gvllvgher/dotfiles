from libqtile import layout
from libqtile.config import Match
from modules.colors import palette

layout_defaults = dict(
    border_focus = palette["light_border"],
    border_normal = palette["dark_border"],
    border_width = 1
)

layouts = [
    layout.Bsp(
        grow_amount = 2,
        border_on_single = False,
        margin = 10,
        **layout_defaults
    ),
    layout.MonadTall(
        margin = 8,
        **layout_defaults
    ),
    #layout.Columns(border_focus_stack='#d75f5f'),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='Alacritty'),
    Match(wm_class='flameshot'),
    Match(wm_class='xfce4-power-manager-settings'),
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
