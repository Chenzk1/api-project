#!/usr/bin/python3 
import pymysql, re
 
db = pymysql.connect("localhost","Chenzk","Chenzk1","myproject",charset="utf8" )
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()    
cbls = []
qxddcy = [] 
sfcp = []
hgnt = []
ffsb = []
# SQL 查询语句
sql = "SELECT * FROM stopfaultreason"
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        if (row[4] == "ls") or row[4] == "ls " or (row[4] == "cb"):
            stopfault = {}       
            stopfault['reason'] = row[1]
            stopfault['time'] = row[2]  
            stopfault['range'] = "%4.f%%" % ((row[2]/(row[3]))*100)                   
            cbls.append(stopfault)
        elif row [4] == "qx" or row[4] == "dd" or row[4] == "cy":
            stopfault = {}       
            stopfault['reason'] = row[1]
            stopfault['time'] = row[2]  
            stopfault['range'] = "%4.f%%" % ((row[2]/(row[3]))*100)                   
            qxddcy.append(stopfault)
        elif row[4] == "sf" or row[4] == "cp":
            stopfault = {}       
            stopfault['reason'] = row[1]
            stopfault['time'] = row[2]  
            stopfault['range'] = "%4.f%%" % ((row[2]/(row[3]))*100)                   
            sfcp.append(stopfault)
        elif row[4] == "hg" or row[4] == "nt":
            stopfault = {}       
            stopfault['reason'] = row[1]
            stopfault['time'] = row[2]  
            stopfault['range'] = "%4.f%%" % ((row[2]/(row[3]))*100)                   
            hgnt.append(stopfault)
        else:
            stopfault = {}       
            stopfault['reason'] = row[1]
            stopfault['time'] = row[2]  
            stopfault['range'] = "%4.f%%" % ((row[2]/(row[3]))*100)                   
            ffsb.append(stopfault)
except:
    print ("Error: unable to fetch data")
db.close()
