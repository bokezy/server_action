# encoding:utf-8
import requests
import random
YOUR_KEY='SCU156152T14435ae80a60fcecdae6da9d67842bca60138c301ed8d'
api = "https://sc.ftqq.com/SCU156152T14435ae80a60fcecdae6da9d67842bca60138c301ed8d.send"
title = "Github"
content = "Actions的信息！！！"+str(random.randint(0,99))
"""
#服务器又炸啦！
##请尽快修复服务器
"""
data = {
   "text":title,
   "desp":content
}
req = requests.post(api,data = data)
