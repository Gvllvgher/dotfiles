-- globals.lua

local api = vim.api
local cmd = vim.cmd
local g = vim.g

-- Line Number color
api.nvim_set_hl(0, 'LineNr', { fg = "#000000"} )

-- Clipboard
api.nvim_set_option("clipboard","unnamed")

-- Colorscheme
cmd.colorscheme "catppuccin"

-- Notify function
vim.notify = require("notify")

-- Globals
g.python3_host_prog = "/usr/bin/python3"
g.airline_theme = 'catppuccin'
g.loaded_ruby_provider = 0
g.loaded_node_provider = 0
g.loaded_perl_provider = 0
g.coc_global_extensions = {
  'coc-json',
  'coc-toml',
  'coc-yaml',
  'coc-git',
  'coc-pyright',
  'coc-lua',
  'coc-powershell',
  'coc-html',
  'coc-highlight',
  'coc-prettier',
  'coc-spell-checker',
  'coc-sh',
  'coc-docker',
  'coc-translator',
  'coc-markdownlint'
}
