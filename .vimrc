" SETTINGS ---- {{{
" Set compatibilty to vim only
set nocompatible

" Auto text wrapping
set wrap "nowrap for no auto wrap

" Encoding
set encoding=utf-8

" Show line numbers
set number relativenumber

" Status bar
set laststatus=2

" Intent width
set shiftwidth=4

" Tab width
set tabstop=4

" Use spaces instead of tabs
set expandtab

" Do not save backup files
set nobackup

" Incrementally highlight while searching
set incsearch

" Case during search
set ignorecase
set smartcase

" Show matching words
set showmatch

" Highlight during search
set hlsearch

" Command history
set history=1000
" }}}

" MAPPINGS ---- {{{
nnoremap <F3> :NERDTreeToggle<CR>
" }}}

" VIMSCRIPT ---- {{{
" Allows folding, use command zc to close folds
augroup filetype_vim
    autocmd!
    autocmd FileType vim setlocal foldmethod=marker
augroup END
" }}}

" PLUGINS ---- {{{
call plug#begin('~/.vim/plugged')
  "Autocomplete plugin. similar to VSCode
  Plug 'neoclide/coc.nvim', {'branch': 'release'}
  Plug 'tpope/vim-fugitive'
  Plug 'prettier/vim-prettier'
  Plug 'vim-airline/vim-airline'
  Plug 'vim-airline/vim-airline-themes'
  Plug 'preservim/nerdtree', {'branch':'master'} |
              \ Plug 'Xuyuanp/nerdtree-git-plugin'
call plug#end()
" }}}

" STATUSLINE ---- {{{
let g:airline_theme='term'
" }}}
