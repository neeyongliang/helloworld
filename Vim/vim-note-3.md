【VIM】vi与vim编辑器（高级篇）
---

## VIM多窗口功能
> vim -o file1 file2 ==>> -o后面可以附加数量n

**注意** :set laststatus=1 同一时间只能一个窗口活动,可以设置为2

#### VIM多窗口编辑
> :split ==>> 创建窗口

> :vsplit ==>> 垂直分割窗口(后面不加filename就不同时编辑一个文件)

#### 分割窗口选项
```shell
:[n]split [++opt] [+cmd] [file]
说明:
n: vim指定在新窗口显示行数,新窗口位于前面
opt:传递vim选项信息给新的窗口会话(必须加上两个加号)
cmd:欲在新窗口中执行的命令
file:指定打开的文件
```

#### 游走在窗口间
```shell
:set mouse=a ==>> 激活鼠标
CTRL + W ==>> 切换窗口
:topleft ==>> 左上角
```

## 窗口移动命令概要
#### 窗口交换
命令|说明|附加|
------|------|------
^Wr|向右或向下轮换窗口||
^W^R| - | - |
^WR|向左或者向上| - |
(n)^Wx|与下一个窗口交换位置|与第n个窗口互换位置|
^W^X| - | - |

#### 改变布局
命令|说明|附加|
------|------|------
^WK|移动窗口至当前屏幕顶端,使用屏幕全部高度||
^WJ|移动窗口至当前屏幕底端,使用屏幕全部高度||
^WH|移动窗口至当前屏幕左端,使用屏幕全部高度||
^WL|移动窗口至当前屏幕右端,使用屏幕全部高度||
^WT|移动窗口至现有分页|^PageUp/^PageDown切换|

## 尺寸调整命令概要
命令或选项|说明|附加|
------|------|------|
^W=|重新调整所有窗口至相同尺寸|以设置的winheight和winwidth设置为准|
:resize -n|减少当前窗口的尺寸|默认减少一行|
:resize +n|增加当前尺寸|默认增加一行|
:resize n|设置当前尺寸||
Zn [ENTER]|设置当前窗口高度n||
^W<|增加当前窗口的宽度|默认增加一栏|
^W>|减少当前窗口的宽度|默认减少一栏|
:vertical resize n|设置当前窗口的宽度|默认值为最大窗口宽度|
winheight选项|进入或创建窗口时,设置其高度至少等于指定值||
winwidth选项|进入或创建窗口时,设置其宽度至少等于指定值||
equalalways选项|窗口数量改变时候把剩余窗口调整为相同尺寸||
eadirection|定义vim实在垂直还是水平位置上调整尺寸||
cmdheight选项|设置命令行高度||
winminheight|定义最小窗口高度||
winminwidth|定义最小窗口的宽度||

## 关闭与离开窗口
命令|说明|
------|------|
:quit!|离开当前窗口|
^Wq|同上|
:close!|关闭当前窗口|
:only!|让当前窗口成为唯一窗口|
^Wo|同上|

------
## vim脚本
#### 配色

```vimrc
    " progressively check highter values... fall out on first "true"
    " (note addition of zero... this guarantees return from function is numeric)
    if strftime("%H") < 6 + 0
    colorscheme darkblue
    echo "setting colorscheme to darkblue"
    elseif strftime("%H") < 12 + 0
    colorscheme morning
    echo "setting colorscheme to morning"
    elseif strftime("%H") < 18 + 0
    colorscheme shine
    echo "setting colorscheme to shine"
    else
    colorscheme evening
    echo "setting colorscheme to evening"
    endif
```

#### 变量
vim变量的作用域（scop）依赖于变量的前缀，通常游如下惯例：

名称|作用域|
------|------|
b|在单一vim缓冲区里被辨识的变量|
w|在单一vim窗口里被辨识的变量|
t|在单一vim分页里被辨识的变量|
g|全局变量，能在任何地方被辨识的变量|
l|局部变量，能在函数内被辨识的变量|
s|在来源的vim脚本里被辨识的变量|
a|函数的参数|
v|vim变量－由vim控制，也是全局变量|

如果不使用前缀，默认是:g 函数内是:l

可以使用let命令指派变量值

```
    :let var = "value"
    echo "currentHour is " . currentHour
    if currentHour < 6+0
        let colorScheme = "darkblue"
    elseif currentHour < 12 + 0
        let colorScheme = "morning"
    elseif currentHour < 18 + 0
        let colorScheme = "shine"
    else
        let colorScheme = "evening"
    echo "seting color scheme to" . colorScheme
    colorscheme colorScheme
```
所以改写上例，不需要执行4次strftime，只需要计算一次currentHour，再判断处理。

**警告**:上例会出现错误！！！

#### execute命令
我们需要一个执行vim命令，且指向参数而非字面字符（如：darkblue），因此需要用到execute

> execute "colorscheme " . colorScheme

execute的估算运算执行：
- 估算丹村的（不加引号）词，词将被按照命令或者表达式，execute将传入的值替换为估算的结果
- 引号括起来的字符串呗视为文字，execute不会试着估算并且返回一个值

#### 定义函数
结构

```
    function myFunction(arg1,arg2...)
        line of code
        another line of code
    endfunction
```

> call myFunction(arg1,arg2...)


#### 不错的vim诀窍

```
    set statusline=%<%t%h%m%r\ \ %a\ %{strftime(\"%c\")}%=0x%B\
    \\ line:%l,\ \ colo:%c%V\ %P
```

> set statusline += \ %{SetTimeOfDayColors()}

**缺点**:消耗资源，浪费。

#### 以全局变量转变vim

```
    function setTimeOfDayColors()
    ...
    endif
    " let g:colors_name = "xyzzy" or colorscheme default
    " if our calculated value is different, call the colorscheme command.
    if g:colors_name !~ colorScheme
        echo "setting color secheme to " . colorScheme
        execute "colorscheme " . colorScheme
    endif
    end function
```

**警告**：colors_name 会提示未定义，因为colorscheme命令尚未执行

#### 数组
> let g:Favcolorschemes = ["darkblue", "morning", "shine", "evening"]

```
    function SetTimeOfDayColors()
    " currentHour will be 0,1,2 or 3
    let g:Favcolorschemes = ["darkblue", "morning", "shine", "evening"]
    let g:CurrentHour = (strftime("%H") + 0) /6
    if g:color_name !~ g:FavcolorSchemes[g:CurrentHour]
        execute "colorscheme " . g:Favcolorschemes[g:CurrentHour]
        echo "execute " "colorscheme " . g:Favcolorschemes[g:CurrentHour]
        redraw
    endif
    endfunction
```

## 通过脚本动态配制文件类型
#### 自动命令
自动命令包括任何合格的vim命令

命令|触发条件|
------|------|
BufNewFile|在vim编辑新文件时触发相关联的命令|
BufReadPre|在vim移向新缓冲区前触发相关联的命令|
BufRead,BufReadPost|在编辑新文件时触发相关联的命令|
BufWrite,BufWritePre|把缓冲区的内容写入文件前触发相关联的命令|
FileType|在触发相关联的命令|
VimResized|在触发相关联的命令|
WinEnter,WinLeave|在触发相关联的命令|
CursorMoved,CursorMovedI|在触发相关联的命令|

总共由80个，格式如下：

> autocmd [group] event pattern [nested] command

元素|说明|
------|------|
group|可选命令组|
event|触发命令的事件|
pattern|匹配文件名模式，用于找出执行命令的文件|
nested|如果出现，表示这个命令能放在其他自动命令中|
command|当事件发生时执行vim命令，函数，用户自定义脚本|

> autocmd CursorMovedI * call CheckFileType()

#### 检查选项
输入20个字符后检测文件类型，输入200个之后不再检测。

```
    function CheckFileType()

    if exists("b:countCheck") == 0
        let b:countCheck = 0
    endif

    let b:countCheck += 1

    " Don't start detecting until apporx. 20 chars.
    if &filetype == "" && b:countCheck > 20 && b:countCheck < 200
        filetype detect
    endif
    endfunction
```

#### 自动命令与组
范例是通过CursorMovedI事件为函数,调用与一个组制造关联.vim提供了augroup命令:

```
    augroup groupname
    ...(other code)...
    augroup end
```

现在为前面的autocmd定义与我们的组制造关联:

```
    augroup newFileDetection
    autocmd CursorMovedI * call CheckFileType()
    augroup END
```

#### 删除自动命令
> autocmd! [group] [event] [pattern]

在检测出文件类型并予以指派或达到200个字符的阈值后,就不需要自动命令定义.于是:

```
    augroup newFileDetection
    autocmd CursorMovedI * call CheckFileType()
    augroup END

    function CheckFileType()

        if exists("b:countCheck") == 0
            let b:countCheck = 0
        endif

        let b:countCheck += 1

        " Don't start detecting until approx. 20 chars.
        if &filetype == "" && b:countCheck > 20 && b:countCheck < 200
        " If we've exceeded the count threshold (200), OR a filetype has been detected
        " delete the autocmd!
        elseif b:countCheck >= 200 || &filetype != ""
            autocmd! newFileDetection
        endif
    endfunction
```
可以在vim中输入一下命令来检测:

> autocmd newFileDetection

**警告**:不要把删除自动组误以为是删除自动命令!

## 关于VIM脚本的其他思考
一个好的vim脚本范例:

```
    autocmd BufWritePre,FileWritePre *.html mark s|call LastMod()|'s
    fun LastMod()
        " if there are more than 20 lines, set our max to 20, otherwise, scan
        " entire file
        if line("$") > 20
            let lastModifiedline = 20
        else
            let lastModifiedline = line("$")
        endif
        exe "1," . lastModifiedline . "g/Last modified: /s/Last modified:
            .*/Last modified: " .
            \ strftime("%Y %b %d")
    end fun
```
说明:

> *.html:限制文件类型->mark s创建一个标记->管道字符,用于分隔vim命令,无特殊含义->调用LastMod->分隔->回到s

#### 再谈变量
vim有5中变量类型

数字,字符串,函数引用,列表,字典

未了正确区分字符串与数字,强在运算时加上0:

> if strftime("%H") < 6 + 0

#### 表达式
vim表达式仅仅能做简单的整数估算

#### 扩展组件
vim提供不少扩展组件与其他脚本语言接口.尤其值得注意的是,其中包括:
**Python**,**Ruby**,**Perl**

#### 再讨论autocmd
autocmd BufRead,BufNewFile *.html set shiftwidth=2
autocmd BufRead,BufNewFile *.c,*.h set shiftwidth=4

#### 内部函数
在帮助文件usr_41.txt里

## 资源
- 脚本
 - http://www.vim.org/scripts/index.php

- 文档
    - help autocmd
    - help scripts
    - help variables
    - help functions
    - help usr_41.txt

内置说明文档是无价之宝
