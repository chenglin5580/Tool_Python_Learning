# git 学习

## git 介绍
> Git是目前世界上最先进的分布式版本控制系统（没有之一）。


## git 安装

- 查看git版本
> git --version

- 下载
[下载地址](https://git-scm.com/downloads)

- 安装完成后配置个人信息
> git config --global user.name "Your Name"  
> git config --global user.email "email@example.com"

## git本地仓库管理

- 基础概念
> git管理分为工作区、暂存区stage和分支  
> git 管理的是修改，而不是整个文件  
> git 有一个HEAD指针

- 初始化
> git init 

- 查看当前git状态
> git status   查看文件状态  
> git log      查看commit历史  
> git log --pretty=oneline 简化log输出信息

- add 文件
> git add readme.txt  
> git add 是将工作区的 **修改** 提交给stage

- commit 文件
> git commit -m "first version"  
> m 代表memory的意思，就是记录  
> git commit 一次性将stage中所有的修改提交给默认分支上

- 删除文件
> rm readme.txt 系统删除命令  
> git rm readme.txt 将分支上的文件也删除


- 文件回退
> git checkout  -- readme.txt  
> checkout **抛弃当前工作区的修改** ，将工作区的内容更换为stage的内容  
> checkout 还是有切换分支的意思，后文再讲  
> 主要应用场景是文件修改错了，但是还没有add提交，非常方便

- stage回退
> git reset HEAD readme.txt  
> stage关于readme的修改恢复到分支相同状态  
> 用处不是很大，针对的是单个文件需要回退 

- 版本回退
> git reset --hard HEAD^  
> git reset --hard 3628164 不需要全部数字，可以前后调整HEAD的位置  
> HEAD表示当前指针位置，HEAD^表示上一个，HEAD^100表示上100个  
> hard 表示全清，恢复到上版本  
> reset 主要针对的是分支操作，不过reset的过程中，顺便把工作区的内容换成了新HEAD的文件


## git 远程链接github

- 链接github
> ssh-keygen -t rsa -C "chenglin5580@163.com"  
> 将本地生成的ssh密钥拷贝到github上  
> 这实际上完成了本地电脑和github的关联  

- 创建一个新的本地仓库链接github上的空库
> git init  
> git add README.md  
> git commit -m "first commit"  
> git remote add origin https://github.com/chenglin5580/aa.git 具体改为仓库地址  
> git push -u origin master


- 链接一个已有的本地库
> git remote add origin https://github.com/chenglin5580/aa.git  
> git push -u origin master
> git remote remove origin  移除一个已有的远程库  
> [remote更多指令详见](file:///C:/Program%20Files%20(x86)/Git/doc/git/html/git-remote.html)


## git 分支管理

- 基础概念
> HEAD指向分支名称(默认master),分支名称指向提交commit

- 创建和合并分支
> git branch dev    创建  
> git checkout dev  切换  
> git checkout -b dev  创建并切换  
> git branch 查询当前分支  
> git merge dev 将dev分支合并到master上  
> git branch -d dev 删除dev分支  

- 解决冲突
> 当master和分支同时进行修改，且不一致时候  
> git merge dev 会失败  
> 文件会出现两个分支的内容，你可以做出选择修改  
> git add read.txt  
> git commite -m "conflict solve"  
> git branch -d dev 删除分支  

- 分支管理策略
> git merge 默认会用fast forward，删除分支后，会丢掉分支信息  
> git merge --no-ff -m "merge with no-ff" dev 可以新提交一个commit  
> git log --graph --pretty=oneline --abbrev-commit 查看提交历史  
> **分支策略**：首先，master分支应该是非常稳定的，也就是仅用来发布新版本，平时不能在上面干活；那在哪干活呢？干活都在dev分支上，也就是说，dev分支是不稳定的，到某个时候，比如1.0版本发布时，再把dev分支合并到master上，在master分支发布1.0版本；你和你的小伙伴们每个人都在dev分支上干活，每个人都有自己的分支，时不时地往dev分支上合并就可以了。  


- 使用github
> 关注好的项目，fork可以在自己账号下面clone一个项目仓库  
> git clone git@github.com:michaelliao/bootstrap.git 从自己仓库clone到本地  
> 本地操作，push和pull  
> github上可以做pull request  














