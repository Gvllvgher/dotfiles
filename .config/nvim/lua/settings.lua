-- options.lua

local g = vim.g
local opt = vim.opt

-- Core
opt.compatible = false -- set nocompatible
opt.encoding = "utf-8" -- encoding
opt.backup = false -- do not save backup files
opt.spell = true -- spellchecking

-- UI
opt.wrap = true -- set false for nowrap - for auto wrapping
opt.number = true -- shows line numbers
opt.relativenumber = true -- use relative line numbers
opt.laststatus = 2 -- status bar
opt.termguicolors = true -- enable 24-bit RGB colors

-- Search
opt.incsearch = true -- incrementally highlight while searching
opt.ignorecase = true -- ignore case while searching
opt.smartcase = true -- match other cases while searching
opt.showmatch = true -- show matching works
opt.hlsearch = true -- highlight during search

-- Tabs, Indent, Folding
opt.shiftwidth = 2 -- indent width
opt.tabstop = 2 -- tab width
opt.expandtab = true -- use spaces instead of tab
opt.smartindent = true -- auto-indent lines
opt.foldmethod = 'marker' -- enable folding

-- Memory, CPU
opt.hidden = true -- enable background buffers
opt.history = 100 -- Remember N lines in history
opt.lazyredraw = true -- faster scrolling
opt.synmaxcol = 240 -- max column for syntax highlighting
opt.updatetime = 250 -- ms to wait for triggering events

-- Globals
g.python3_host_prog="/usr/bin/python3"
g.airline_theme='term'
g.loaded_ruby_provider=0
g.loaded_node_provider=0
g.loaded_perl_provider=0
