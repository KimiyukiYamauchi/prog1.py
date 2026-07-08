### ~/.vimrc

```vim

"========================
" 基本設定
"========================

" 構文（シンタックス）ハイライトを有効にする
syntax on

" ファイルタイプごとのプラグイン・インデント設定を有効にする
filetype plugin indent on

" 行番号を表示する
set number

" カーソル位置からの相対行番号を表示する
" （上下への移動がしやすくなる）
set relativenumber

" 検索時に大文字・小文字を区別しない
set ignorecase

" 検索文字列に大文字が含まれる場合だけ
" 大文字・小文字を区別する
set smartcase

" 検索結果をハイライト表示する
set hlsearch

" 入力中に検索結果をリアルタイムで表示する
set incsearch

" True Color（24bitカラー）を有効にする
" カラースキームがきれいに表示される
set termguicolors

" Backspaceキーで
" ・自動インデント
" ・改行
" ・挿入開始位置
" を削除できるようにする
set backspace=indent,eol,start

" Undo履歴をファイルに保存し、
" Vimを終了してもUndoできるようにする
set undofile


"========================
" Python設定
"========================

" Python用設定グループ
augroup python

    " このグループの既存設定を削除
    autocmd!

    " PythonファイルではTab文字ではなくスペースを使用する
    autocmd FileType python setlocal expandtab

    " Tab文字を4文字分として表示する
    autocmd FileType python setlocal tabstop=4

    " << や >> のインデント幅を4文字にする
    autocmd FileType python setlocal shiftwidth=4

    " Tabキー入力時のスペース数を4文字にする
    autocmd FileType python setlocal softtabstop=4

    " 前の行のインデントを自動的に引き継ぐ
    autocmd FileType python setlocal autoindent

    " if、for、while、defなどに応じて
    " インデントを自動調整する
    autocmd FileType python setlocal smartindent

    " 88文字目にガイドラインを表示
    " （Blackフォーマッタの推奨行長）
    autocmd FileType python setlocal colorcolumn=88

augroup END


"========================
" キーマッピング
"========================

let mapleader = " "

" 保存
nnoremap <Leader>w :w<CR>

" Python実行
nnoremap <Leader>r :w<CR>:!python3 %<CR>
```