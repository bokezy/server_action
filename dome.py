# encoding:utf-8
import requests
import random

S = """
#服务器又炸啦！
##请尽快修复服务器

这是push操作

"""
YOUR_KEY='SCT20668TNGrIOR9Sa4wor8vCVaywKP48'
api = "https://sctapi.ftqq.com/{}.send".format(YOUR_KEY)
title = "Github"
content = "Actions的信息！！！"+str(random.randint(0,99))
data = {
   "text":title,
   "desp":content
}
req = requests.post(api,data = data)
