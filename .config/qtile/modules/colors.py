from catppuccin import Flavour

theme = Flavour.mocha()

palette = dict(
    text = theme.text.hex,
    red = theme.red.hex,
    blue = theme.blue.hex,
    light_background = theme.surface2.hex,
    dark_background = theme.crust.hex,
    dark_border = theme.mantle.hex,
    light_border = theme.overlay0.hex
    )
