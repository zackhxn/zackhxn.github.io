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
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42676739/1716900298577-fd11fa3a-0113-46db-93db-8fadbce02646.png#averageHue=%23fdfcfc&clientId=u1fa0ad9c-38e4-4&from=paste&height=398&id=kAS6S&originHeight=358&originWidth=648&originalType=binary&ratio=0.8999999761581421&rotation=0&showTitle=false&size=16035&status=done&style=none&taskId=ud342ab5b-2bc9-47b4-96b5-5d2239fd5df&title=&width=720.0000190734868)
注册成功后即可进行登录。
进入文本标注系统后，你会发现什么内容也没有，别着急，因为管理员还未给你派发任务。

![image.png](https://cdn.nlark.com/yuque/0/2024/png/42676739/1716900759066-8524beac-4976-4bd3-9057-6c5c6e004608.png#averageHue=%23f2f2f2&clientId=u1fa0ad9c-38e4-4&from=paste&height=208&id=JYIji&originHeight=187&originWidth=1503&originalType=binary&ratio=0.8999999761581421&rotation=0&showTitle=false&size=11003&status=done&style=none&taskId=u883d88fe-6cf0-4a57-8acb-54aa6e5200f&title=&width=1670.000044239893)
如果你获得了新任务，那界面应该是这样的：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42676739/1716901389750-9efdb47c-89e6-424f-9c54-cecc1f298252.png#averageHue=%23f5f3f1&clientId=u1fa0ad9c-38e4-4&from=paste&height=456&id=avwSY&originHeight=410&originWidth=1511&originalType=binary&ratio=0.8999999761581421&rotation=0&showTitle=false&size=71673&status=done&style=none&taskId=u0a257309-b0d3-4ad4-9b3e-768e56b263b&title=&width=1678.8889333642571)
点击进入待标注的项目，即可查看自己被分配的标注任务。
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42676739/1716901417890-17bc9b7b-94f2-4366-82c8-8ee209a2081c.png#averageHue=%23faf8f6&clientId=u1fa0ad9c-38e4-4&from=paste&height=570&id=hexnQ&originHeight=513&originWidth=1502&originalType=binary&ratio=0.8999999761581421&rotation=0&showTitle=false&size=78868&status=done&style=none&taskId=u4df3b15a-eeae-41c3-b601-1aad80cd0ac&title=&width=1668.8889330993475)
点击“去标注”即可开始标注任务。在标注任务的开始会有使用说明的教程，不妨耐心看一遍。
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42676739/1716901434390-9710081b-a10f-455d-b23b-e312b7e1b3cb.png#averageHue=%23aaa9a8&clientId=u1fa0ad9c-38e4-4&from=paste&height=901&id=hCOu2&originHeight=811&originWidth=1490&originalType=binary&ratio=0.8999999761581421&rotation=0&showTitle=false&size=185257&status=done&style=none&taskId=u37ba7463-4bd7-438e-a62f-8f4a349afaf&title=&width=1655.5555994128015)
每一次标注都需要先在文档中选择需要的实体，然后给它选择标签，确认无误后进行提交，就完成了一次标注。
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42676739/1716901509234-3737df96-97ca-4dbb-bc5c-e0eafd32da5e.png#averageHue=%23f8f6f3&clientId=u1fa0ad9c-38e4-4&from=paste&height=851&id=BZYcW&originHeight=766&originWidth=1524&originalType=binary&ratio=0.8999999761581421&rotation=0&showTitle=false&size=398352&status=done&style=none&taskId=u602d1f33-3c94-4be2-8508-fd7adfaf46d&title=&width=1693.3333781913486)
等所有待标注实体都完成之后，点击完成标注即可结束任务。
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42676739/1716901544752-7c3beeef-371c-46ef-8747-8775ec9abc5f.png#averageHue=%23f9f6f3&clientId=u1fa0ad9c-38e4-4&from=paste&height=803&id=LugOs&originHeight=723&originWidth=1508&originalType=binary&ratio=0.8999999761581421&rotation=0&showTitle=false&size=391962&status=done&style=none&taskId=u6b8fdeb1-c15e-4cb7-928c-cdc453b5011&title=&width=1675.5555999426206)
## 管理员
管理员是标注任务的发起者，在系统登录管理员账号后，点击“新建标注项目”即可开始一个新项目。
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42676739/1716900985233-2602105a-da12-40f4-9f94-941859280f48.png#averageHue=%23f6f3f1&clientId=u1fa0ad9c-38e4-4&from=paste&height=719&id=sFJoo&originHeight=647&originWidth=1497&originalType=binary&ratio=0.8999999761581421&rotation=0&showTitle=false&size=119666&status=done&style=none&taskId=uddcfe921-59a5-463b-ad69-f585967541e&title=&width=1663.33337739662)
在新建标注项目中需写明项目名称以及项目简介。
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42676739/1716901060381-15c478c5-118d-40a2-9918-05155eb4ee68.png#averageHue=%23f2f1ef&clientId=u1fa0ad9c-38e4-4&from=paste&height=539&id=z27cq&originHeight=485&originWidth=943&originalType=binary&ratio=0.8999999761581421&rotation=0&showTitle=false&size=48015&status=done&style=none&taskId=u74a6f55d-15c0-4212-9011-99fa087ea60&title=&width=1047.7778055344106)
新建任务成功之后即可在系统管理页中查看不同任务的详细配置。在标注人员一栏中可以指定该任务需要的标注员。
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42676739/1716901105736-3f4b57b0-62ab-4d08-bb9a-61042cf5593f.png#averageHue=%23fcfcfb&clientId=u1fa0ad9c-38e4-4&from=paste&height=458&id=xvYbE&originHeight=412&originWidth=1505&originalType=binary&ratio=0.8999999761581421&rotation=0&showTitle=false&size=33243&status=done&style=none&taskId=u97635fa0-9cb1-430c-b93a-d9c9454dbb8&title=&width=1672.222266520984)
在标注文本一栏中可以选择需要标注的PDF文档。
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42676739/1716901133773-8c3fbced-e046-4f36-8dc3-dc6500372418.png#averageHue=%23fdfcfc&clientId=u1fa0ad9c-38e4-4&from=paste&height=483&id=b3bzU&originHeight=435&originWidth=1505&originalType=binary&ratio=0.8999999761581421&rotation=0&showTitle=false&size=26593&status=done&style=none&taskId=u909f8414-a35c-4360-89d0-fb16c64d980&title=&width=1672.222266520984)
从本地上传文档之后，文档会自动进行格式转换。
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42676739/1716901203484-b51dcd63-706f-4665-ba2c-c13bfdf7e2e1.png#averageHue=%23b4b4b4&clientId=u1fa0ad9c-38e4-4&from=paste&height=593&id=ISlNM&originHeight=534&originWidth=1494&originalType=binary&ratio=0.8999999761581421&rotation=0&showTitle=false&size=35851&status=done&style=none&taskId=uc2c138b6-86f0-46ee-b5cf-d0afaadabfa&title=&width=1660.0000439749836)![image.png](https://cdn.nlark.com/yuque/0/2024/png/42676739/1716901211764-2b89d079-7e62-4037-84a8-82c9150acb77.png#averageHue=%23fcfcfb&clientId=u1fa0ad9c-38e4-4&from=paste&height=389&id=UcY5f&originHeight=350&originWidth=1493&originalType=binary&ratio=0.8999999761581421&rotation=0&showTitle=false&size=27104&status=done&style=none&taskId=u3121cc06-e061-449b-8b3e-21563c577fd&title=&width=1658.888932834438)
如果转换成功，会显示“转换成功”字样，之后便可进行设定“标注标签”的步骤。
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42676739/1716901219703-b3501ca9-9194-4f09-8197-2dc7043aabd0.png#averageHue=%23fcfbfb&clientId=u1fa0ad9c-38e4-4&from=paste&height=419&id=znQDo&originHeight=377&originWidth=1495&originalType=binary&ratio=0.8999999761581421&rotation=0&showTitle=false&size=27385&status=done&style=none&taskId=u22130e5f-7ae2-444d-9503-8e9a5edefe1&title=&width=1661.111155115529)
在“标注标签”一栏中需要写明需要标注的标签KEY以及标签名称。
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42676739/1716901230310-a9ea1c36-09ec-4b9b-b1dc-a21a66bbe0fd.png#averageHue=%23989797&clientId=u1fa0ad9c-38e4-4&from=paste&height=473&id=AB1od&originHeight=426&originWidth=1489&originalType=binary&ratio=0.8999999761581421&rotation=0&showTitle=false&size=30656&status=done&style=none&taskId=u1c1f6f4c-db22-485d-be30-a33ec6467e1&title=&width=1654.444488272256)
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42676739/1716901333713-6b37d940-a7af-4f29-bc22-5928d339dfdf.png#averageHue=%23bebebe&clientId=u1fa0ad9c-38e4-4&from=paste&height=459&id=Pt0YB&originHeight=413&originWidth=870&originalType=binary&ratio=0.8999999761581421&rotation=0&showTitle=false&size=20059&status=done&style=none&taskId=ubaa13c67-6c91-478f-85d5-5bab51630a4&title=&width=966.6666922745889)
最后在任务分配一栏可选择一篇文本对应的标注员数量。
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42676739/1716901350994-dd4b4baf-28d1-41fc-85dd-feba8d9b4f0e.png#averageHue=%23fcfcfc&clientId=u1fa0ad9c-38e4-4&from=paste&height=533&id=c2zZX&originHeight=480&originWidth=635&originalType=binary&ratio=0.8999999761581421&rotation=0&showTitle=false&size=15959&status=done&style=none&taskId=u84b444e3-33cf-4436-9c02-6e703ee1c65&title=&width=705.5555742463953)
等所有标注员都完成任务之后，即可进行标注数据的导出。
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42676739/1716901362032-4fead6c3-8ff1-446b-827f-0565f7db1257.png#averageHue=%23fcfcfb&clientId=u1fa0ad9c-38e4-4&from=paste&height=469&id=KTEGy&originHeight=422&originWidth=1499&originalType=binary&ratio=0.8999999761581421&rotation=0&showTitle=false&size=36096&status=done&style=none&taskId=u71876c4d-eb49-4f8b-99e9-174f31e522f&title=&width=1665.5555996777111)
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42676739/1716901609331-c2af1b88-a6b2-4bda-abcb-c3db13e52cab.png#averageHue=%23fcfbfb&clientId=u1fa0ad9c-38e4-4&from=paste&height=534&id=KgS7C&originHeight=481&originWidth=1526&originalType=binary&ratio=0.8999999761581421&rotation=0&showTitle=false&size=45289&status=done&style=none&taskId=u379afa13-c0d9-4605-b230-9ea4affea47&title=&width=1695.5556004724397)
## 科研用户
科研用户是智能挖掘系统的主要使用者。在标注任务完成之后，用户可以选择点击“导出模型配置”，来导出用于配置大模型的模型配置文件。
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42676739/1716901638788-78bf5025-9bbb-474f-9df0-2f09ec9a1a68.png#averageHue=%23fcfcfc&clientId=u1fa0ad9c-38e4-4&from=paste&height=441&id=L8b9K&originHeight=397&originWidth=1524&originalType=binary&ratio=0.8999999761581421&rotation=0&showTitle=false&size=37729&status=done&style=none&taskId=u842ed883-2f3b-4db9-a5ad-0b918ac9e59&title=&width=1693.3333781913486)
配置文件会被保存到用户本地，同时系统会自动跳转到智能挖掘子系统。
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42676739/1716901658729-bbca9e12-fcb7-4500-89df-d3bc774e9aa2.png#averageHue=%23f9f8f7&clientId=u1fa0ad9c-38e4-4&from=paste&height=591&id=gcEI2&originHeight=532&originWidth=991&originalType=binary&ratio=0.8999999761581421&rotation=0&showTitle=false&size=56772&status=done&style=none&taskId=ua439d07f-6a8d-45f3-b3f0-ca5068de82c&title=&width=1101.1111402805948)
智能挖掘子系统主要分左侧的设置区域和主要的聊天对话区域。
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42676739/1716952849523-f56e3003-8fdc-4c81-bfe1-9dd6cc7e0996.png#averageHue=%23fdfcfc&clientId=u03f7a0c3-178e-4&from=paste&height=914&id=F6411&originHeight=914&originWidth=1907&originalType=binary&ratio=0.8999999761581421&rotation=0&showTitle=false&size=82127&status=done&style=none&taskId=u32a0c407-447e-45db-9946-7ce599b4db7&title=&width=1907)
点击左侧的“Modelfiles”即可进入模型的配置界面，点击“导入模型文件”，即可将刚刚保存的模型配置文件进行导入。
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42676739/1716952870384-acb72b22-b693-4452-8c97-55ac2ccacb67.png#averageHue=%23fcfbfb&clientId=u03f7a0c3-178e-4&from=paste&height=241&id=qkkUm&originHeight=241&originWidth=797&originalType=binary&ratio=0.8999999761581421&rotation=0&showTitle=false&size=12890&status=done&style=none&taskId=u3a6f4814-5fde-4946-90b4-d301c07f52c&title=&width=797)
导入成功之后，点击此按钮来查看配置的详细信息。

![image.png](https://cdn.nlark.com/yuque/0/2024/png/42676739/1716952886307-abdedd2c-af1d-4081-b3ab-f77801cf4cfe.png#averageHue=%23fbfbfa&clientId=u03f7a0c3-178e-4&from=paste&height=266&id=OXBwe&originHeight=266&originWidth=790&originalType=binary&ratio=0.8999999761581421&rotation=0&showTitle=false&size=18628&status=done&style=none&taskId=u686c6de6-8779-457c-acee-61dd67a7892&title=&width=790)
可对该配置的图标、名称、描述、内容等进行确认或再一次的修改，无误之后点击“保存并更新”，完成模型配置。
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42676739/1716952914253-65d64580-a555-4405-9de8-ab927b649f38.png#averageHue=%23fdfbfb&clientId=u03f7a0c3-178e-4&from=paste&height=873&id=sNRSc&originHeight=873&originWidth=885&originalType=binary&ratio=0.8999999761581421&rotation=0&showTitle=false&size=65040&status=done&style=none&taskId=ue8bbee6a-c332-4728-92bb-08d42b84456&title=&width=885)
直接点击该模型，或在聊天区域的左上角选择刚刚创建的模型，都可以开始与配置的大模型进行对话。
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42676739/1716953089650-e2b3a939-2564-4788-bdc9-91038379524a.png#averageHue=%23fbfbfa&clientId=u03f7a0c3-178e-4&from=paste&height=274&id=um6Wk&originHeight=274&originWidth=790&originalType=binary&ratio=0.8999999761581421&rotation=0&showTitle=false&size=18109&status=done&style=none&taskId=u46d611d8-2cc3-4942-be04-8f5b6af177e&title=&width=790)![image.png](https://cdn.nlark.com/yuque/0/2024/png/42676739/1716953105717-392241a7-b209-4024-904f-ef137b321e44.png#averageHue=%23fcfcfb&clientId=u03f7a0c3-178e-4&from=paste&height=725&id=f5eOd&originHeight=725&originWidth=1690&originalType=binary&ratio=0.8999999761581421&rotation=0&showTitle=false&size=76417&status=done&style=none&taskId=ue486e3d6-f477-49e2-a923-7e07405d977&title=&width=1690)
选择预设的提问内容，或在输入框中自行输入想要询问的内容，都可以开启与智能挖掘模型的对话。
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42676739/1716953185302-a106ff91-0290-4ca9-b106-bc5f46d9b499.png#averageHue=%23fdfdfd&clientId=u03f7a0c3-178e-4&from=paste&height=909&id=lo3bj&originHeight=909&originWidth=1415&originalType=binary&ratio=0.8999999761581421&rotation=0&showTitle=false&size=54235&status=done&style=none&taskId=u679fe032-9b22-4dd9-8222-11e4c7bfc5c&title=&width=1415)
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42676739/1716906299245-1062ac91-0912-441e-8907-7bb0ee25eba1.png#averageHue=%23fefdfd&clientId=u1fa0ad9c-38e4-4&from=paste&height=824&id=LYUNr&originHeight=742&originWidth=1336&originalType=binary&ratio=0.8999999761581421&rotation=0&showTitle=false&size=92620&status=done&style=none&taskId=u0fe92243-1559-4554-8914-4520f3578ed&title=&width=1484.4444837687938)

# **技术支持**
如果你遇到了任何问题，都欢迎你来我们的项目地址[https://csse.nas.buaanlsde.cn/BY2306092/24teama_itas](https://csse.nas.buaanlsde.cn/BY2306092/24teama_itas) 提出您宝贵的建议。
