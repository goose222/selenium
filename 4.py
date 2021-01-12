import json

import pymysql

conn = pymysql.connect(
    host="10.10.10.10",  # mysql服务器地址
    port=3306,  # 端口号
    user='groupleader',  # 用户名
    passwd='onlyleaders',  # 密码
    db='nsfc',  # 数据库名称
)
cursor = conn.cursor()  # 创建并返回游标

fp = open(r"C:\Users\63093\PycharmProjects\untitled1\data3.json", 'r', encoding="utf-8")
text = fp.read()
text = json.loads(text)
print(type(text))


# ON DUPLICATE KEY UPDATE StartandEndTime=%s  更新用
for i in text["results"]:

    command = 'insert IGNORE into nsfc_zizhu (名称,批准号,项目类别,项目负责人,批准年度,资助经费,依托单位,起止年月,申请代码) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'

    n = cursor.execute(command, (i['名称'], i['批准号'], i['项目类别'], i['项目负责人'], i['批准年度'], i['资助经费'], i['依托单位'], i['起止年月'], i['申请代码']))

    conn.commit()

cursor.close()
conn.close()