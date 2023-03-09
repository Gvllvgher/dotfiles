return {
  "catppuccin/nvim",
  name = 'catppuccin',
  config = function ()
    require("catppuccin").setup({
      flavor = "mocha",
          background = { -- :h background
        light = "latte",
        dark = "mocha",
      },
      transparent_background = true,
      show_end_of_buffer = false, -- show the '~' characters after the end of buffers
      term_colors = false,
      dim_inactive = {
          enabled = false,
          shade = "dark",
          percentage = 0.15,
      },
      no_italic = false, -- Force no italic
      no_bold = false, -- Force no bold
      styles = {
          comments = { "italic" },
          conditionals = { "italic" },
          loops = {},
          functions = {},
          keywords = {},
          strings = {},
          variables = {},
          numbers = {},
          booleans = {},
          properties = {},
          types = {},
          operators = {},
      },
      color_overrides = {},
      custom_highlights = {},
      integrations = {
          --cmp = true,
          coc_nvim = true,
          nvimtree = true,
          treesitter = true,
          notify = true,
          --telescope = true,
          --mini = false,
        -- For more plugins integrations please scroll down (https://github.com/catppuccin/nvim#integrations)
      },
    })
  end
}
