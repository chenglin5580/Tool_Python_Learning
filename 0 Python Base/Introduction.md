# Python Introduction

[TOC]

## Author
> Guido van Rossum

## Reason
> 开发缘由：1989年圣诞节期间，为了打发无聊的圣诞节而编写的一个编程语言。  

## Application
> YouTube、Instagram，还有国内的豆瓣。很多大公司，包括Google、Yahoo等，甚至NASA（美国航空航天局）都大量地使用Python

## 优点
优雅、明确、简单

缺点：
- 速度慢
- 不能加密

## 安装
[廖雪峰安装教学](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014316090478912dab2a3a9e8f4ed49d28854b292f85bb000)

## Python的解释器
- CPython  
- IPython  
- PyPy  
- Jython  
- IronPython  


## Python的启动
- Windows下直接在CMD里面运行Python
- 记得加入环境变量

## 文本编辑器
- [Sublime Text](http://www.sublimetext.com/)
- [Notepad ++](https://notepad-plus-plus.org/)


## 字符串编码
- 计算机只能处理数字，如果要处理文本，就必须先把文本转换为数字才能处理
- 最新的Python 3版本中，字符串是以Unicode编码的

#### 常用编码
- ASCII编码
- GB2312编码
- Unicode(UTF-8编码)

#### 常用操作
- ord()函数获取字符的整数表示
- chr()函数把编码转换为对应的字符
- 以Unicode表示的str通过encode()方法可以编码为指定的bytes
- .    # -*- coding: utf-8 -*- 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。申明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的，必须并且要确保文本编辑器正在使用UTF-8 without BOM编码···

## 结构
- .#是注释
- 当语句以冒号:结尾时，缩进的语句视为代码块

## 好的教学
- [廖雪峰](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)
- [小甲鱼零基础入门学习Python](http://blog.fishc.com/category/python)






