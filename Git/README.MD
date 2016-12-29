ALL ABOUT GIT
------

- 这是一个说明文件，来自wikinee，记录我的Git学习。下面所说的均有图形和命令行两种操作方式，图形略。

##day01
- Git 分布式版本控制系统，linus
- 注意：git config -global参数表示对本机上所有git仓库使用配置

###01.创建版本库(repository)
- git init
- git add readme1.txt
- ...
- git add readmen.txt
- git commit -m "worote a README file" 
- //最好写上注释，防止被遗忘。

###02.要随时掌握工作区的状态
- git status
- git reset -hard commit_id(可以使用HEAD^表示上一个，HEAD^^上上个，如果太多就表示成类似HEAD~100)
- git log 查看历史
- git reflog 回到未来

###03.直接丢弃
- git checkout --file
- git reset HEAD file
- //可以把HEAD看作一个指针

###04.删除
- git rm

###05.连接
- git remote add origin https://github.com/wikinee/repo-name.git(除了http格式，还可以使用邮箱格式，git@github.com:wikinee/repo-name.git)

###06.克隆
- git clone https://github.com/wikinee/repo-name.git(除了http格式，还可以使用邮箱格式，git@github.com:wikinee/repo-name.git)

###07.分支
- git branch 查看
- git branch <name> 创建
- git checkout <name>切换
- git checkout -b <name>创建并切换到当前分支
- git merge <name>合并某分支到当前分支
- git branch -d <name>删除分支

-------
##day02
###08.冲突处理
- 当Git无法自动合并分支的时候，必须解决冲突，之后再提交。
- 用git -log -graph查看，若采用fast forward，必须是不发生冲突的分支

###09.分支管理策略
- 禁用 fast forward
- git merge --no-ff -m "merge with on-ff" <name>
- git log --graph --pretty=online --abbrev-commiting

###10.Bug分支
- git stash//遇到bug分支，需要保存现场
- git checkout bug_branch//需要在哪个分支修复，就切换到哪个分支
- git checkout -b issue_number//在那个分支建立零时分支
- ...bug fix...
- git branch -d issue_number//删除分支，恢复现场
- git stash list//所有现场
- //下面有两种方法：
- A.git stash pop//恢复后删除stash
- B.git stash apple stash{0}
-   git stash drop stash{0}

###11.Feature分支
- 添加新的小功能。
- 开发一个新的Feature，最好选择建立一个新的分支
- 如果要弄丢一个没有被合并过的分支，可以通过git branch -D <name>强制删除

###12.多人协作
- 远程查看
- git remote (-v)

###13.推送分支
- master分支是主分支，应该与远程实时同步
- dev分支是开发分支，也要同步
- bug分支是本地修复分支，不需要同步
- feature是否需要同步，取决于是否开发新的功能。

###14.抓取分支
- 查看远程库信息，使用git remote -v
- 本地新建的分支如果不推送到远程，对其他人就是不可见的。
- 总结
- ————多人协作的步骤：
- A.首先，可以试图用git push origin branch-name 推送自己的修改；
- B.如果推送失败，则因为远程分支比你本地的分支更新，需要用git pull试图合并；
- C.如果合并冲突，需要解决冲突，并在本地提交
- D.没有冲突或者解决掉冲突后，再用git push origin branch-name推送，就能推送成功
- 如果git pull显示提示“no tracking information”，则说明本地分支和远程分支的连接关系没有创建，需要下列命令：
- git branch -set-upstream branch-name origin/branch-name

###15.标签管理
- git tag <name>用于新创建一个标签，默认是HEAD，也可以指定一个commit_id;
- git tag -a <tagname> -m "balabala..." 可以指定信息标签
- git tag -s <tagname> -m "balabala..."可以使用PGP签名标签
- git tag可以查看所有标签

###16.操作标签
- git push origin <tagname>可以推送本地一个标签
- git push origin -tags可以推送本地未推送过的标签
- git tag -d <tagname> 可以删除一个本地标签
- git push origin:refs/tags/<tagname>可以远程删除一个标签
- git push -u origin master
 
###17.使用github
- 如何参与故意开源项目？
- Fork it；
- clone it；
- 可以推送pull request

###18.自定义git
- 忽略文件：
- 需要写.gitignore
- #注释
- q.txt
- b.db
- c.pw
- ...
- .gitignore本身也要上传到版本库，也可以进行版本管理

###19.配置别名
- git config --global alias.<简写名> <完整名>
- git reset HEAD file把转存区的修改去掉
- 也可在.git/config 文件【alias】标签中修改。

###20.搭建git服务器(略)
###21.管理公钥Gitosis(略)
###22.控制权限(Gitolite)
==========================================================================================================
COMPELET DATE:Ste.02,2015


