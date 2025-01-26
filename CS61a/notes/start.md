# Terminal

## Git Bash

### 本地操作

cd //进入文件夹

cd .. //回到上一个文件夹

ls //列出当前文件夹中的文件

mkdir+文件夹名 //新建文件夹

touch+文件名 //新建文件

rm 文件名.文件类型 //删除文件 

rm -r 文件夹 //删除文件夹,要返回上一级文件夹中操作

### 远程仓库管理

git init //将当前文件夹初始化为本地仓库

$ ssh-keygen -t rsa -C "你的邮箱"//创建SSH key

~/.ssh 查找是否有ssh文件。

git remote add + name + link //本地连接远程仓库

git remote -v//查看连接是否建立

### 文件上传

git add -A //将改动的文件加入上传缓冲区

git commit -m "注释" //为本次上传文件添加注释

git push -u name branch //上传文件 当前只有主分支master

 git commit --amend -m "修改的内容"//修改注释。

# Python

`python3 --version` 查看python版本

`python` 进入 python coding

`exit()` or ` Ctrl-Z` 退出coding

# Text Editor

vscode,vim,...

# Using Terminal

CLI (command line interface)命令行界面

GUI(graphical user interface)图形用户界面

# Organize files

`ls` 列出当前文件夹的目录

`cd ~` 返回主目录

`cd Desktop` 进入Desktop文件夹

`mkdir` 创建文件夹

use `python3 ok --local` to execut codes locally

`-i` to run codes interactively

`-m doctest` to run the doctests in code files.s

