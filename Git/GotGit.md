Git 权威指南
------

[开源地址](http://www.worldhello.net/gotgit/)

## 第01章 初识Git
### 设置字符集

```
git config --global core.quotepath false //UTF-8字符集
git config --global i18n.logOutputEncoding gbk //GBK字符集
```

## 第02章 Git独奏
### Git初始化
```
//创建版本库以及第一次提交
git --version //查看 git 版本
git config --global user.name "wiki"
git config --global user.email neeyongliang@gmail.com
git init 名字(可选)

//git alias
sudo git config --system alias.br branch
sudo git config --system alias.ci "commit -s" //带签名的commit
sudo git config --system alias.co checkout
sudo git config --system alias alias.st "-p status"

//关于参数
--system:对应/etc/gitconfig
--global:对应$HOME/.gitconfig
无参数:单个 repo 里面的设置
--unset:清除设置

git grep "要搜索的内容"
git add/commit 

git rev-parse --git-dir //显示版本库.git 路径
git rev-parse --show-toplevel //显示工作区根目录
git rev-parse --show-prefix //相当于工作区根目录的目录
git rev-parse --show-cdup //当前目录退回到工作区根目录的深度

//命令git config可以用于读取和更改INI配置文件的内容。使用命令git config <section>.<key>，
//来读取INI配置文件中某个配置的键值。例如读取[core]小节的bare的属性值，可以用如下命令:
$ git config core.bare
false 

//如果想更改或设置INI文件中某个属性的值也非常简单，命令格式是：
// git config <section>.<key> <value>。可以用如下操作：
$ git config a.b something
$ git config x.y.z others

//效果
[a]
        b = something

[x "y"]
        z = others

//替换默认的 INI 文件
GIT_CONFIG=test.ini git config a.b.c.d
git commit --allow-empty -m "who does it?" //允许不做任何修改的提交
git log --pretty=fuller
git commit --amend --allow-empty --reset-author

```

### Git暂存区
```
$ git status -s //以简单方式显示
$ git diff --cached //提交暂存区与版本仓库文件的差异
$ git diff --stated //提交任务和版本仓库中的差异

// 理解 Git 暂存区
$ git reset HEAD //重写仓库至 master 目前所指向的目录树
$ git rm --cached <file> //直接删除暂存区文件,工作区不做改变
$ git checkout -- <file> //丢弃本次对file的修改

// git diff
$ git ls-tree -l HEAD //指向当前目录树, -l 表示大小
$ git clean -nd //可以查看将要删除的文件,确认之后↓
$ git clean -fd //清除当前没有加入版本库中的文件和目录
$ git write-tree //写入目录树

// 不要使用 git commit -a

//暂存状态
$ git stash
$ git stash [list | apply | stash | clear |stash]
```

### Git重置
```
$ git log --graph --pretty=oneline
$ git reset --hard HEAD^ // 回退状态, 丢弃修改,慎用!
$ git reflog show master | head -5 //删选日志

// git reset
// 不会重置引用
$ git reset [-q] [<commit>] [--] <paths>... 
git reset HEAD <paths> //取消 git add <path>

//会重置引用
$ git reset [--soft | --mixed | --hard | --merge | --keep] [-q] [<commit>] 
--soft: 只改变引用,不改变修改的内容
--mixed: 缺省参数
--hard: 强制回退版本
```

### 恢复进度
```
$ git clean -nd //查看将要删除
$ git clean -fd //删除
$ git status -sb

$ git stash
$ git stash apply //不使用pop, 原因是可能多次用到
$ git ls-files // 跟 ls 类似,但是是 git 的 ls
$ git add -i //选择提交
```

## Git 和声

