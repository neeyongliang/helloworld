【VIM】程序员的vim
------

主要讨论:
- 折叠
- 自动智能缩排
- 关键字与字典补全
- 标签与扩展标签
- 语法高亮显示编写(自定)
- Quickfix, Vim缩小版IDE

## 折叠与大纲
vim提供6种定义,创建,操纵折叠的方式.
方式|功能|
------|------|
manual|以标准的vim结构定义折叠跨越的范围,类似移动命令|
indent|折叠与折叠的层次,对应于文本的缩排与shiftwidth选项值|
expr|以正则表达式折叠|
syntax|折叠对应于文件所用的程序语言语义(如C语言程序块)|
diff|以两个文件间的差异定义折叠|
marker|以文件中的预定义(亦可以由用户定义)标记指定折叠边界|

#### 折叠命令
约20个,折叠命令均以z开头(纸折起来像z)

名字|功能|
------|------|
zA|递归切换折叠状态|
zC|递归关闭折叠|
zD|递归删除折叠|
zE|去除所有折叠|
zf|创建折叠,当前行开始到光标移动(借助移动命令)后的位置|
countzF|创建涵盖count行的折叠|
zM|设置foldlevel选项为0|
zN,zn|设置(zN)或复位(zn)foldenable选项|
zo|递归打开折叠|
za|切换一个折叠的状态|
zc|关闭一个折叠|
zd|删除一个折叠|
zi|切换foldenable选项的值|
zj,zk|移动到下一个(zj)或者前一个(zk)折叠|
zm,zr|递减zm或者递增zr的foldlevel选项的值|
zo|打开一个折叠|

**警告**:不要把删除折叠与一般删除命令混淆

实例:

> 3zF 或者 2zfj

#### 智能缩排
> :set cindent //设置方法,set

vim提供下列缩排方式(按照复杂度排列):
- autoindent, 模仿vi的autoindent,差异在于删除后光标的位置
- smartindent, 能识别C语法元素
- cindent, 高级C语言识别
- indentexpr, 能自定义表达式

#### 关键字与字典词汇补全
一些组合键,大都是:

> Ctrl + X,Ctrl + [key]

的方式执行

## 语法高亮
> syntax enable

> syntax on

#### 标识符高亮显示
> :highlight indentifier

> :highlight indentifier guifg=red //重新定义标识符颜色

#### 保存修改
> :set runtimepath+=~/.vim/after/syntax

> :highlight ...

#### 心得
  
**不是**什么情况下都要使用**vim**!学习vim更多的应该学习一种思想.推荐熟练操作:
- Sublime
- JetBrains
