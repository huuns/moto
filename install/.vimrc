set nocompatible
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'gmarik/Vundle.vim'
Plugin 'tpope/vim-fugitive'
Plugin 'L9'
Plugin 'git://git.wincent.com/command-t.git'
Plugin 'file:///home/gmarik/path/to/plugin'
Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}
Plugin 'The-NERD-tree'
Plugin 'nathanaelkane/vim-indent-guides'
call vundle#end()            " required
"filetype plugin indent on    " required



let NERDTreeWinPos = "left"
nmap <F7> :NERDTreeToggle<CR>
filetype on

nmap <F8> :IndentGuidesToggle<CR>


set number
set hlsearch
set autowrite 
set autoread 
set showmatch 


let python_highlight_all = 1


autocmd VimEnter * :IndentGuidesEnable

let g:indent_guides_start_level=1 
let g:indent_guides_guide_size=1

let g:indent_guides_auto_colors = 0
"autocmd VimEnter,Colorscheme * :hi IndentGuidesOdd  guibg=red   ctermbg=3
"autocmd VimEnter,Colorscheme * :hi IndentGuidesEven guibg=green ctermbg=4
"hi IndentGuidesOdd  guibg=red   ctermbg=3
"hi IndentGuidesEven guibg=green ctermbg=4
hi IndentGuidesOdd  guibg=red   ctermbg=5
hi IndentGuidesEven guibg=green ctermbg=6
set ts=2 sw=2 et
