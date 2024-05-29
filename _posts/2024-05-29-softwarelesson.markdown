---
layout:     post
title:      "软工实验-多领域智能文本标注与挖掘系统"
subtitle:   " \"用户说明书\""
date:       2024-05-29 11:51:00
author:     "zack"
catalog: true
tags:
    - 软件工程
    - 大模型
    - 标注
    - 挖掘
---
> 开发的一个多领域智能文本标注与挖掘系统，我主要负责了第二个挖掘子系统的开发，以及两个系统的连接。

# 前言
欢迎来到多领域智能文本标注与挖掘系统（ITAS），本文档旨在让任何人轻松上手该系统，无论你是新手小白还是资深专家，我们都为你准备了详细的使用指南，让你快速上手，事半功倍！
# 系统简介
在当今的知识时代，研究人员依赖于大量的文献资料以探寻新知和获取数据。这些文献承载着重要的学术成果和研究进展，然而，直接从这些PDF格式的文献中标注和提取所需信息，却是一项充满挑战的任务。手工进行此类工作不仅耗时巨大，而且极易出错，这对于追求精准和效率的学术研究来说，显然是不可接受的。为了解决以上问题，我们提出可扩展的多领域智能文本标注与挖掘系统（ITAS），旨在协助研究人员高效准确地进行科学文献中段落和实体的标注，以及自动化提取和挖掘预设定义的关键信息。

1. 多领域支持：系统设计将充分考虑到不同研究领域的特殊需求，通过模块化和可配置的标注预设，支持广泛的学科和专业领域，包括但不限于社会科学、生物医学、工程技术等。
2. 协助标注：提供一个用户友好的界面和工具集，协助研究人员进行科学文献的段落和实体标注工作。通过预定义的标注规则和模板，以及智能推荐和辅助功能，大幅降低标注工作的难度和时间成本，提高标注数据的准确性和一致性。
3. 自动化抽取：利用先进的大语言模型和自然语言处理技术，如GPT系列，实现从标注的文档中自动化提取和挖掘预设定义的关键信息。系统将支持小样本学习，以适应数据稀缺的研究场景，从而提高从大量未标注文本中快速准确提取信息的能力。

# 开始使用
本系统无需任何的手动安装步骤，所有的功能都已在公网ip中上线！只需访问[http://ye-sun.com:1855/](http://ye-sun.com:1855/login) 即可开始轻松的标注与挖掘之旅~
## 标注员
进入系统之后，首先需要注册账户。
![image.png](https://zackhxn.github.io/img/2024-05-29-softwarelesson_1.png)
注册成功后即可进行登录。
进入文本标注系统后，你会发现什么内容也没有，别着急，因为管理员还未给你派发任务。

![image.png](https://zackhxn.github.io/img/2024-05-29-softwarelesson_2.png)
如果你获得了新任务，那界面应该是这样的：
![image.png](https://zackhxn.github.io/img/2024-05-29-softwarelesson_3.png)
点击进入待标注的项目，即可查看自己被分配的标注任务。
![image.png](https://zackhxn.github.io/img/2024-05-29-softwarelesson_4.png)
点击“去标注”即可开始标注任务。在标注任务的开始会有使用说明的教程，不妨耐心看一遍。
![image.png](https://zackhxn.github.io/img/2024-05-29-softwarelesson_5.png)
每一次标注都需要先在文档中选择需要的实体，然后给它选择标签，确认无误后进行提交，就完成了一次标注。
![image.png](https://zackhxn.github.io/img/2024-05-29-softwarelesson_6.png)
等所有待标注实体都完成之后，点击完成标注即可结束任务。
![image.png](https://zackhxn.github.io/img/2024-05-29-softwarelesson_7.png)
## 管理员
管理员是标注任务的发起者，在系统登录管理员账号后，点击“新建标注项目”即可开始一个新项目。
![image.png](https://zackhxn.github.io/img/2024-05-29-softwarelesson_8.png)
在新建标注项目中需写明项目名称以及项目简介。
![image.png](https://zackhxn.github.io/img/2024-05-29-softwarelesson_9.png)
新建任务成功之后即可在系统管理页中查看不同任务的详细配置。在标注人员一栏中可以指定该任务需要的标注员。
![image.png](https://zackhxn.github.io/img/2024-05-29-softwarelesson_10.png)
在标注文本一栏中可以选择需要标注的PDF文档。
![image.png](https://zackhxn.github.io/img/2024-05-29-softwarelesson_11.png)
从本地上传文档之后，文档会自动进行格式转换。
![image.png](https://zackhxn.github.io/img/2024-05-29-softwarelesson_12.png)![image.png](https://zackhxn.github.io/img/2024-05-29-softwarelesson_13.png)
如果转换成功，会显示“转换成功”字样，之后便可进行设定“标注标签”的步骤。
![image.png](https://zackhxn.github.io/img/2024-05-29-softwarelesson_14.png)
在“标注标签”一栏中需要写明需要标注的标签KEY以及标签名称。
![image.png](https://zackhxn.github.io/img/2024-05-29-softwarelesson_15.png)
![image.png](https://zackhxn.github.io/img/2024-05-29-softwarelesson_16.png)
最后在任务分配一栏可选择一篇文本对应的标注员数量。
![image.png](https://zackhxn.github.io/img/2024-05-29-softwarelesson_17.png)
等所有标注员都完成任务之后，即可进行标注数据的导出。
![image.png](https://zackhxn.github.io/img/2024-05-29-softwarelesson_18.png)
![image.png](https://zackhxn.github.io/img/2024-05-29-softwarelesson_19.png)
## 科研用户
科研用户是智能挖掘系统的主要使用者。在标注任务完成之后，用户可以选择点击“导出模型配置”，来导出用于配置大模型的模型配置文件。
![image.png](https://zackhxn.github.io/img/2024-05-29-softwarelesson_20.png)
配置文件会被保存到用户本地，同时系统会自动跳转到智能挖掘子系统。
![image.png](https://zackhxn.github.io/img/2024-05-29-softwarelesson_21.png)
智能挖掘子系统主要分左侧的设置区域和主要的聊天对话区域。
![image.png](https://zackhxn.github.io/img/2024-05-29-softwarelesson_22.png)
点击左侧的“Modelfiles”即可进入模型的配置界面，点击“导入模型文件”，即可将刚刚保存的模型配置文件进行导入。
![image.png](https://zackhxn.github.io/img/2024-05-29-softwarelesson_23.png)
导入成功之后，点击此按钮来查看配置的详细信息。

![image.png](https://zackhxn.github.io/img/2024-05-29-softwarelesson_24.png)
可对该配置的图标、名称、描述、内容等进行确认或再一次的修改，无误之后点击“保存并更新”，完成模型配置。
![image.png](https://zackhxn.github.io/img/2024-05-29-softwarelesson_25.png)
直接点击该模型，或在聊天区域的左上角选择刚刚创建的模型，都可以开始与配置的大模型进行对话。
![image.png](https://zackhxn.github.io/img/2024-05-29-softwarelesson_26.png)![image.png](https://zackhxn.github.io/img/2024-05-29-softwarelesson_27.png)
选择预设的提问内容，或在输入框中自行输入想要询问的内容，都可以开启与智能挖掘模型的对话。
![image.png](https://zackhxn.github.io/img/2024-05-29-softwarelesson_28.png)
![image.png](https://zackhxn.github.io/img/2024-05-29-softwarelesson_29.png)

# **技术支持**
如果你遇到了任何问题，都欢迎你来我们的项目地址[https://csse.nas.buaanlsde.cn/BY2306092/24teama_itas](https://csse.nas.buaanlsde.cn/BY2306092/24teama_itas) 提出您宝贵的建议。
