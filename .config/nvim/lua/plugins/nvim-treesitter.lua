return {
  "nvim-treesitter/nvim-treesitter",
  build = ":TSUpdate",
  config = function()
    require'nvim-treesitter.configs'.setup {
      ensure_installed = { "c",
                          "lua",
                          "vim",
                          "query",
                          "bash",
                          "dockerfile",
                          "gitcommit",
                          "gitignore",
                          "html",
                          "json",
                          "markdown",
                          "python",
                          "regex",
                          "yaml",
                          "terraform",
                          "hcl"
      },
      -- Install parsers synchronusly
      sync_install = false,
      -- Auto install parsers
      auto_install = true,
      -- Highlighting
      highlight = {
        enabled = true,
        additional_vim_regex_highlighting = false,
      },
   }
 end,
}
