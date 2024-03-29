-- keys.lua

local function map(mode, lhs, rhs, opts)
  local options = { noremap=true, silent=true }
  if opts then
    options = vim.tbl_extend('force', options, opts)
  end
  vim.api.nvim_set_keymap(mode, lhs, rhs, options)
end

map('n', '<F3>', ':NvimTreeToggle<CR>')

vim.api.nvim_command('inoremap <silent><expr> <Tab> coc#pum#visible() ? coc#pum#confirm() : "\\<Tab>"')
