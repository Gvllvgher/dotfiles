require("core.lazy")
require("core.settings")
require("core.keys")
require("core.treesitter")

require("catppuccin").setup({
  flavour = "mocha",
})

vim.cmd.colorscheme "catppuccin"
