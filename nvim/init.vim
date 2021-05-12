let mapleader = ","
filetype plugin on

call plug#begin('~/.config/nvim/plugged')
    Plug 'gmarik/Vundle.vim'
    Plug 'suan/vim-instant-markdown', {'rtp': 'after'}
    Plug 'preservim/NERDTree'
    Plug 'tiagofumo/vim-nerdtree-syntax-highlight'
    Plug 'ryanoasis/vim-devicons'
    Plug 'tpope/vim-surround'
    Plug 'PotatoesMaster/i3-vim-syntax'
    Plug 'vim-python/python-syntax'
    Plug 'ap/vim-css-color'
    Plug 'tpope/vim-commentary'
    Plug 'danilo-augusto/vim-afterglow'
    Plug 'mattn/emmet-vim'
    Plug 'w0rp/ale'
    Plug 'andymass/vim-matchup'
    Plug 'itchyny/lightline.vim'
    Plug 'jiangmiao/auto-pairs'
    Plug 'HerringtonDarkholme/yats.vim'
    Plug 'neoclide/coc.nvim', {'do': { -> coc#util#install()}}
call plug#end()

set guioptions-=m
set guioptions-=T
set guioptions-=r
set guioptions-=l
set guifont=Comic\ Mono:style=Normal:h14

syntax on

set re=0
set title
set go=a
set mouse=nicr
set mouse=a
set path+=**
set wildmenu
set wildmode=longest,list,full
set incsearch
set hidden
set nobackup
set noswapfile
set t_Co=256
set clipboard=unnamedplus
set grepprg=grep\ -nH\ $*
set whichwrap+=<,>,h,l
set incsearch
set lazyredraw
set magic
set showmatch
set mat=2
set encoding=utf8
set ai
set si
set wrap
set smartcase
set nocompatible
set hlsearch
set ignorecase
set smartcase
set backspace=indent,eol,start
set autoindent
set nostartofline
set laststatus=2
set confirm
set number
set expandtab
set smarttab
set shiftwidth=4
set softtabstop=4
set background=dark
set showmode
set showcmd
set cmdheight=2
set splitbelow splitright
set noruler
set updatetime=300
set shortmess+=c

map Y y$
map <C-j> <C-W>j
map <C-k> <C-W>k
map <C-h> <C-W>h
map <C-l> <C-W>l

noremap <silent> <C-Left> :vertical resize +3<CR>
noremap <silent> <C-Right> :vertical resize -3<CR>
noremap <silent> <C-Up> :resize +3<CR>
noremap <silent> <C-Down> :resize -3<CR>

let g:lightline = {'colorscheme': 'OldHope'}
let g:tex_flavor = "latex"
let g:vimwiki_menu = "Vimwiki"

nnoremap <silent> <Leader>html :-1read $HOME/.vim/.skeleton.html<CR>5jf>a
nnoremap <silent> <Leader>c :-1read $HOME/.vim/.skeleton.c<CR>3jA
nnoremap <silent> <Leader>+ :-1read $HOME/.vim/.skeleton.cpp<CR>4jA

au CursorHoldI * stopinsert
au InsertEnter * silent! let updaterestore=&updatetime | set updatetime=60000 | silent! execute "!setxkbmap -option caps:swapescape" | redraw!
au InsertLeave * silent! let &updatetime=updaterestore | silent! execute "!setxkbmap -option" | redraw!

map <C-e> :NERDTreeToggle<CR>
let g:NERDTreeDirArrowExpandable = '►'
let g:NERDTreeDirArrowCollapsible = '▼'
let NERDTreeShowLineNumbers=1
let NERDTreeMinimalUI = 1
let g:NERDTreeWinSize = 45
let g:NERDTreeWinPos = "right"

let g:instant_markdown_autostart = 0
let g:instant_markdown_browser = "qutebrowser"
map <silent> <Leader>md :InstantMarkdownPreview<CR>
map <silent> <Leader>ms :InstantMarkdownStop<CR>

let g:python_highlight_all = 1

"autocmd FileType * setlocal formatoptions-=c formatoptions-=r formatoptions-=o
vnoremap . :normal .<CR>
nnoremap S :%s//g<Left><Left>

let g:vimwiki_ext2syntax = {'.Rmd': 'markdown', '.rmd': 'markdown','.md': 'markdown', '.markdown': 'markdown', '.mdown': 'markdown'}
let g:vimwiki_list = [{'path': '~/Documents/vimwiki/main',
                     \ 'path_html': '~/Documents/vimwiki/html',
                     \ 'auto_export': 1, 'syntax': 'markdown',
                     \ 'ext': '.md'}]
cnoremap w!! execute 'silent! write !sudo tee % >/dev/null' <bar> edit!
autocmd BufWritePre * %s/\s\+$//e
autocmd BufWritePre * %s/\n\+\%$//e
autocmd BufWritePre *.[ch] %s/\%$/\r/e
autocmd BufRead,BufNewFile Xresources,Xdefaults,xresources,xdefaults set filetype=xdefaults
autocmd BufWritePost Xresources,Xdefaults,xresources,xdefaults !xrdb %

nnoremap <silent> <Leader>/ :let @/ = ""<CR>
nnoremap <silent> <Leader>t gt
nnoremap <silent> <Leader>T gT

inoremap <silent><expr> <TAB>
      \ pumvisible() ? "\<C-n>" :
      \ <SID>check_back_space() ? "\<TAB>" :
      \ coc#refresh()
inoremap <expr><S-TAB> pumvisible() ? "\<C-p>" : "\<C-h>"
inoremap <silent><expr> <c-space> coc#refresh()
function! s:check_back_space() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~# '\s'
endfunction
inoremap <silent><expr> <cr> pumvisible() ? coc#_select_confirm()
                              \: "\<C-g>u\<CR>\<c-r>=coc#on_enter()\<CR>"
nmap <silent> [g <Plug>(coc-diagnostic-prev)
nmap <silent> ]g <Plug>(coc-diagnostic-next)
nmap <silent> gd <Plug>(coc-definition)
nmap <silent> gy <Plug>(coc-type-definition)
nmap <silent> gi <Plug>(coc-implementation)
nmap <silent> gr <Plug>(coc-references)
nnoremap <silent> K :call <SID>show_documentation()<CR>
function! s:show_documentation()
  if (index(['vim','help'], &filetype) >= 0)
    execute 'h '.expand('<cword>')
  elseif (coc#rpc#ready())
    call CocActionAsync('doHover')
  else
    execute '!' . &keywordprg . " " . expand('<cword>')
  endif
endfunction
xmap <leader>f  <Plug>(coc-format-selected)
nmap <leader>f  <Plug>(coc-format-selected)
augroup mygroup
  autocmd!
  autocmd FileType typescript,json setl formatexpr=CocAction('formatSelected')
  autocmd User CocJumpPlaceholder call CocActionAsync('showSignatureHelp')
augroup end
xmap <leader>a  <Plug>(coc-codeaction-selected)
nmap <leader>a  <Plug>(coc-codeaction-selected)
nmap <leader>ac  <Plug>(coc-codeaction)
nmap <leader>qf  <Plug>(coc-fix-current)
if has('nvim-0.4.0') || has('patch-8.2.0750')
  nnoremap <silent><nowait><expr> <C-f> coc#float#has_scroll() ? coc#float#scroll(1) : "\<C-f>"
  nnoremap <silent><nowait><expr> <C-b> coc#float#has_scroll() ? coc#float#scroll(0) : "\<C-b>"
  inoremap <silent><nowait><expr> <C-f> coc#float#has_scroll() ? "\<c-r>=coc#float#scroll(1)\<cr>" : "\<Right>"
  inoremap <silent><nowait><expr> <C-b> coc#float#has_scroll() ? "\<c-r>=coc#float#scroll(0)\<cr>" : "\<Left>"
  vnoremap <silent><nowait><expr> <C-f> coc#float#has_scroll() ? coc#float#scroll(1) : "\<C-f>"
  vnoremap <silent><nowait><expr> <C-b> coc#float#has_scroll() ? coc#float#scroll(0) : "\<C-b>"
endif
command! -nargs=0 Format :call CocAction('format')
command! -nargs=? Fold :call   CocAction('fold', <f-args>)
command! -nargs=0 OR   :call   CocAction('runCommand', 'editor.action.organizeImport')
nnoremap <silent><nowait> <space>a  :<C-u>CocList diagnostics<cr>
nnoremap <silent><nowait> <space>e  :<C-u>CocList extensions<cr>
nnoremap <silent><nowait> <space>c  :<C-u>CocList commands<cr>
nnoremap <silent><nowait> <space>o  :<C-u>CocList outline<cr>
nnoremap <silent><nowait> <space>s  :<C-u>CocList -I symbols<cr>
nnoremap <silent><nowait> <space>j  :<C-u>CocNext<CR>
nnoremap <silent><nowait> <space>k  :<C-u>CocPrev<CR>
nnoremap <silent><nowait> <space>p  :<C-u>CocListResume<CR>
let g:coc_global_extensions = [
    \ 'coc-snippets',
    \ 'coc-tsserver',
    \ 'coc-eslint',
    \ 'coc-prettier',
    \ 'coc-json',
    \ 'coc-python',
    \ 'coc-html',
    \ 'coc-css',
    \ 'coc-go',
    \ 'coc-html-css-support',
    \ 'coc-jedi',
    \ 'coc-sh',
    \ ]
nmap <F2> <Plug>(coc-rename)


colorscheme afterglow
