【VIM】vi与vim编辑器（基础篇）
------
## Command mode：

### 行内移动
>    h ==>> ←

>    j ==>> ↓

>    k ==>> ↑

>    l ==>> →

>    \+  ==>>  向下移动到非空行

>    \-  ==>> 向上移动到非空行

>    n + space ==>> 右移n列
>    0 / [[ ==>> [HOME]

>    $ / ]] ==>> [END]

>   ～ ==>> 更变大小写

>    e，E ==>> 单词结尾

>   cw ==>> change words

>   dw ==>> delete words删除一个单词，但是de删除包括空格的单词

>   yw ==>> yank words

>   D ==>> d$

>   ^  ==>> 移动到当前行第一个非空处

>  n| ==>> 移动至第n列

>  ( ==>> 移动到当前句子开头（同0）

>  ) ==>> 移动到下个句子开头（同$）

>  { ==>> 移动到当前段开头

>  } ==>> 移动到下段开头

>  [[ ==>> 移动到这节文件开头

>  ]] ==>> 移动到下节文件开头

>  fx ==>> 向后搜索

>  Fx ==>> 向前搜索

>  ； ==>> 重复上一条搜索命令，方向相同

>  ， ==>> 重复上一条搜索命令，方向相反

### 行间移动
>    H ==>> 当前屏幕首行行首（页面不滚动）

>    M ==>> 当前屏幕中行行首（页面不滚动）

>    L ==>> 当前屏幕尾行行首（页面不滚动）

>    G ==>> 最后一行

>    nG ==>> 第n行（配合:set nu显示行号/:set nonu隐藏行号）

>    gg ==>> 1G, 第一行

>    n + ENTER ==>> 向下移动n行

>    \: + n ==>> 跳转到n行

### 翻页移动
>    ctrl + f ==>> page front

>    ctrl + b ==>> page front

>    ctrl + d ==>> page down

>    ctrl + u ==>> page up

>    z + ENTER ==>> 当前屏幕第首行行首（页面滚动）

>    z + .  ==>> 当前屏幕中行行首（页面滚动）

>    z + ～ ==>> 当前屏幕尾行行首（页面滚动）

### 查找与替换
>   /word 向下查找word

>   ?word 向上查找word

>   n/N 重复/相反重复上一个动作

>   :n1,[n2, $]s/word1/word2/gc 从第n1行到n2行（使用$代表到最后一行），参数c会在替换的时候confirm

> /与?搜索运算符可配合其他命令使用：

> d?move ==>> 删除到上个move

### 删除、复制和粘贴
>    x，X ==>> delete, Backspace

>   nx ==>> 向后删除n列

>   (n)dd ==>> 删除（n）行

>   d1G / dG / y1G / yG ==>> 从该行到第1行/尾行删除/复制

>   d$ / d0 / y$ / y0 ==>> 从该列到结尾/开头删除

>   (n)yy ==>> 复制（n）行

>   p，P ==>> 将已复制的资料粘贴到下/上一行

>   J ==>> 将该行与下一行合并

>   10cj ==>> 向下删除10行

>   u ==>> 恢复上一个动作

>   ctrl + r ==>> 重复前一个动作

### 文本信息
>   ctrl + G ==>> 显示当前行数

## Insert mode：
>    i，I ==>> i：在光标处插入，I：在第一个非空字符处插入

>    a，A ==>> a：i之后开始插入，A：Addition，相当于$a,与I相反

>    r，R ==>> r：替换一次，R：一直替换，直到ESC

## Last line mode：
>    :w! ==>> 强制写入

>    :q! ==>> 强制退出

>    ZZ ==>> 无更改，退出；有更改，保存退出

>    :n1,n2 w [filename] ==>> 将n1到n2行保存如filename

>    :! command  ==>> 暂时离开vi编辑器，执行command命令（如：ls ～）

>    :set nu/set nonu ==>> 显示/隐藏行号