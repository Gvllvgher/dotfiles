-- globals.lua

local g = vim.g

-- Colorscheme
vim.cmd.colorscheme "catppuccin"

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
  'coc-python',
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
