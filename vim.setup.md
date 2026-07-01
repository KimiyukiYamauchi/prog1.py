### ~/.vimrc

```vim

"========================
" 基本設定
"========================
syntax on
filetype plugin indent on

set number
set relativenumber

set ignorecase
set smartcase
set hlsearch
set incsearch

set termguicolors

set backspace=indent,eol,start

set undofile

"========================
" Python設定
"========================
augroup python
    autocmd!
    autocmd FileType python setlocal expandtab
    autocmd FileType python setlocal tabstop=4
    autocmd FileType python setlocal shiftwidth=4
    autocmd FileType python setlocal softtabstop=4
    autocmd FileType python setlocal autoindent
    autocmd FileType python setlocal smartindent
    autocmd FileType python setlocal colorcolumn=88
augroup END

" F5でPython実行
nnoremap <F5> :w<CR>:!python3 %<CR>
```