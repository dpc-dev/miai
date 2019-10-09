#/usr/bin/python3
# -*- codung: utf-8 -*-
import requests,pymysql,hashlib,random
import st,re
# s = requests.Session()
# headers = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",

# "Accept-Encoding":"gzip, deflate, br",
# "Accept-Language": "zh-CN,zh;q=0.9",
# "Cache-Control": "max-age=0",
# "Connection": "keep-alive",
# "Cookie": "csrftoken=pDsjieyCNCVP63KYzg6rfECIxa8hSPqE2wuWdoNrJPWELcqG66MchtMBQqvmXuaT; sessionid=j5jtwe0hl2kz2lcdxdkroioy3h0naqff",
# "Host": "127.0.0.1",
# "Referer": "http://127.0.0.1/reg",
# "Sec-Fetch-Mode": "navigate",
# "Sec-Fetch-Site": "same-origin",
# "Sec-Fetch-User": "?1",
# "Upgrade-Insecure-Requests": "1",
# "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1",
# }
# a = requests.get("http://127.0.0.1" ,headers={"Cookie":"csrftoken=bIvVXDETurMxovzv13ZGNh4rQpG7XiWIsJvjgjzUHWTTigC8Vi1NhjcoVV93vjTs; sessionid=kosil7pnbm5hoe1zed7874aqi7q1lp01"})
# print(a.text)
# ct = st.ZhenziSmsClient('https://sms_developer.zhenzikj.com',102927,'eb38637e-5ff8-4791-9db9-f941cd488cc1')
# code=random.randint(10000,100000)
# req = ct.send('18671289536', '尊敬的用户您好,欢迎加入千寻大家庭，您本次的验证码为%s,有效时间为5分钟'%code)
# print(req)
with open(r"C:\Users\Administrator\Desktop\Web技术\代码\dpcapi - 副本\static\images\g5.jpg") as f:
    data = f.read()
db = pymysql.connect("localhost","root","1478963520.ai","qxun",charset='utf8',use_unicode=True,)
cur = db.cursor()

cur.execute("insert into user_pic values(1001,1,%s)"%data)
db.commit()
cur.close()
db.close()