#encouding=utf-8
from flask import Flask, jsonify, redirect, request
import pymysql

app = Flask(__name__, static_url_path='', static_folder='front')


@app.route("/")
def index():
    return redirect("index.html")

@app.route("/api/currentUser")
def currentUser():
    user = {
      'name': '仲锴',
      'avatar': 'https://gw.alipayobjects.com/zos/rmsportal/BiazfanxmamNRoxxVxka.png',
      'userid': '00000001',
      'notifyCount': 12,
    }
    return jsonify(user)

@app.route('/api/users')
def users():
    users = [
    {
      'key': '1',
      'name': 'John Brown',
      'age': 32,
      'address': 'New York No. 1 Lake Park',
    },
    {
      'key': '2',
      'name': 'Jim Green',
      'age': 42,
      'address': 'London No. 1 Lake Park',
    },
    {
      'key': '3',
      'name': 'Joe Black',
      'age': 32,
      'address': 'Sidney No. 1 Lake Park',
    }
    ]
    return jsonify(user)


@app.route('/api/login/account', methods = ['POST'])
def login_account():
    print(request.values)
    send = {
            'status': 'ok',
            'currentAuthority': 'admin',
            'type': ''
        }  
    if (request.form.get('password') == '000000' and request.form.get('userName') == 'CPMC'): 
        send = {
            'status': 'ok',
            'currentAuthority': 'admin',
            'type':'' 
        }

    if (request.form.get('password') == '111111' and request.form.get('userName') == 'zju'):
        send = {
            'status': 'ok',
            'currentAuthority': 'user',
            'type':'' 
        } 
    return jsonify(send)


@app.route('/api/productdata', methods = ['GET'])
def getProductdata():
    db = pymysql.connect("localhost","Chenzk","Chenzk1","myproject" )
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    yearData = [] 
    # SQL 查询语句
    sql = "SELECT * FROM productionm1"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            yeardata = {}            
            yeardata['x'] = "%d月" % row[0]
            yeardata['y'] = row[1]
            yearData.append(yeardata)
    except:
        print ("Error: unable to fetch data")
    db.close()

    db = pymysql.connect("localhost","Chenzk","Chenzk1","myproject",charset="utf8" )
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()    
    monthData = [] 
    # SQL 查询语句
    sql = "SELECT * FROM production1"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            monthdata = {}       
            monthdata['month'] = 1     
            monthdata['id'] = row[0]
            monthdata['name'] = row[1]            
            monthdata['num'] = row[2]
            monthData.append(monthdata)
    except:
        print ("Error: unable to fetch data")
    db.close()
   
    productData = {
    'monthData' : monthData,
    'yearData' : yearData
    }   
    return jsonify(productData)

@app.route('/api/stopdata', methods = ['GET'])
def getStopdata():
    db = pymysql.connect("localhost","Chenzk","Chenzk1","myproject",charset="utf8" )
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()    
    stopCause = [] 
    # SQL 查询语句
    sql = "SELECT * FROM stopcause"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            stopcause = {}       
            stopcause['id'] = row[0]
            stopcause['reason'] = row[1]
            stopcause['time'] = row[4]
            stopcause['range'] = "%.2f%%" % ((row[4]/(row[2]-row[3]))*100)          
            stopCause.append(stopcause)
    except:
        print ("Error: unable to fetch data")
    db.close()

    db = pymysql.connect("localhost","Chenzk","Chenzk1","myproject",charset="utf8" )
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()    
    stopCausePie = [] 
    # SQL 查询语句
    sql = "SELECT * FROM stopcause"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            stopcausepie = {}       
            if row[4] != 0:
                stopcausepie['x'] = row[1]
                stopcausepie['y'] = row[4]       
                stopCausePie.append(stopcausepie)
    except:
        print ("Error: unable to fetch data")
    db.close()

    db = pymysql.connect("localhost","Chenzk","Chenzk1","myproject",charset="utf8" )
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()    
    stopFaultPie = [] 
    # SQL 查询语句
    sql = "SELECT * FROM stopfaultpie"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            stopfaultpie = {}       
            stopfaultpie['x'] = row[1]
            stopfaultpie['y'] = row[2]       
            stopFaultPie.append(stopfaultpie)
    except:
        print ("Error: unable to fetch data")
    db.close()

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
                stopfault['range'] = "%.2f%%" % ((row[2]/(row[3]))*100)                   
                cbls.append(stopfault)
            elif row [4] == "qx" or row[4] == "dd" or row[4] == "cy":
                stopfault = {}       
                stopfault['reason'] = row[1]
                stopfault['time'] = row[2]  
                stopfault['range'] = "%.2f%%" % ((row[2]/(row[3]))*100)                   
                qxddcy.append(stopfault)
            elif row[4] == "sf" or row[4] == "cp":
                stopfault = {}       
                stopfault['reason'] = row[1]
                stopfault['time'] = row[2]  
                stopfault['range'] = "%.2f%%" % ((row[2]/(row[3]))*100)                   
                sfcp.append(stopfault)
            elif row[4] == "hg" or row[4] == "nt":
                stopfault = {}       
                stopfault['reason'] = row[1]
                stopfault['time'] = row[2]  
                stopfault['range'] = "%.2f%%" % ((row[2]/(row[3]))*100)                   
                hgnt.append(stopfault)
            else:
                stopfault = {}       
                stopfault['reason'] = row[1]
                stopfault['time'] = row[2]  
                stopfault['range'] = "%.2f%%" % ((row[2]/(row[3]))*100)                   
                ffsb.append(stopfault)
    except:
        print ("Error: unable to fetch data")
    db.close()

    stopRadar = [
    {
        "name": "停机工时（h）",
        "label": "冲杯-拉伸区",
        "value": 147,
    },{
        "name": "停机工时（h）",
        "label": "辅助设备",
        "value": 20,
    },{
        "name": "停机工时（h）",
        "label": "清洗-打底-彩印区",
        "value": 42,
    },{
        "name": "停机工时（h）",
        "label": "烘干-内涂区",
        "value": 7,
    },{
        "name": "停机工时（h）",
        "label": "缩翻-成品区",
        "value": 62,
    },
    ]
    stopData = {
    'stopCause' : stopCause,
    'stopCausePie' : stopCausePie,
    'stopFaultPie' : stopFaultPie,
    'stopRadar' : stopRadar,
    'cbls':cbls,
    'qxddcy':qxddcy,
    'sfcp':sfcp,
    'hgnt':hgnt,
    'ffsb':ffsb,
    }     
    return jsonify(stopData)

@app.route('/api/rejectdata', methods = ['GET'])
def getRejectdata():
    db = pymysql.connect("localhost","Chenzk","Chenzk1","myproject",charset="utf8" )
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()    
    rejectYear = [] 
    # SQL 查询语句
    sql = "SELECT * FROM reject"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            rejectyear = {}       
            rejectyear['month'] = row[0]
            rejectyear['totalProduct'] = row[1]
            rejectyear['qualifyProduct'] = row[2]       
            rejectyear['totalWaste'] = row[3]                          
            rejectYear.append(rejectyear)
    except:
        print ("Error: unable to fetch data")
    db.close()

    db = pymysql.connect("localhost","Chenzk","Chenzk1","myproject",charset="utf8" )
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()    
    rejectMonth = [] 
    # SQL 查询语句
    sql = "SELECT * FROM reject"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            rejectmonth = {}       
            rejectmonth['x'] = "%d月" % row[0]
            rejectmonth['y'] = (row[1] - row[2])                        
            rejectMonth.append(rejectmonth)
    except:
        print ("Error: unable to fetch data")
    db.close()
    db = pymysql.connect("localhost","Chenzk","Chenzk1","myproject",charset="utf8" )
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()    
    rejectPercent = [] 
    # SQL 查询语句
    sql = "SELECT * FROM reject"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            rejectpercent = {}       
            rejectpercent['x'] = "%d月" % row[0]
            rejectpercent['y'] = ( (row[1]-row[2])/row[1] )
            rejectPercent.append(rejectpercent)
    except:
        print ("Error: unable to fetch data")
    db.close()

    db = pymysql.connect("localhost","Chenzk","Chenzk1","myproject",charset="utf8" )
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()    
    rejectFenbu = [] 
    # SQL 查询语句
    sql = "SELECT * FROM rejectfenbu"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            rejectfenbu = {}       
            rejectfenbu['x'] = row[1]
            rejectfenbu['y'] = row[2]
            rejectFenbu.append(rejectfenbu)
    except:
        print ("Error: unable to fetch data")
    db.close()
    rejectData = {
    'rejectYear' : rejectYear,
    'rejectMonth' : rejectMonth,    
    'rejectPercent' : rejectPercent,
    'rejectFenbu': rejectFenbu,
    }     
    return jsonify(rejectData)

@app.route('/api/fake_list', methods = ["GET"])
def getFakeList():
    db = pymysql.connect("localhost","Chenzk","Chenzk1","myproject",charset="utf8" )
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()    
    list = [] 
    # SQL 查询语句
    sql = "SELECT * FROM person"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            person = {}       
            if row[4] != 0:
                person['ID'] = row[0]
                person['name'] = row[1]
                person['department'] = row[2]                       
                person['days'] = row[3]
                person['position'] = row[4]                                
                list.append(person)
    except:
        print ("Error: unable to fetch data")
    db.close()
    return jsonify(list)
#   'GET /api/project/notice': getNotice,
#   'GET /api/activities': getActivities,
#   'GET /api/rule': getRule,
#   'POST /api/rule': {
#     $params: {
#       pageSize: {
#         desc: '分页',
#         exp: 2,
#       },
#     },
#     $body: postRule,
#   },
#   'POST /api/forms': (req, res) => {
#     res.send({ message: 'Ok' });
#   },
#   'GET /api/tags': mockjs.mock({
#     'list|100': [{ name: '@city', 'value|1-100': 150, 'type|0-2': 1 }],
#   }),
#   'GET /api/fake_list': getFakeList,
#   'GET /api/fake_chart_data': getFakeChartData,
#   'GET /api/profile/basic': getProfileBasicData,
#   'GET /api/profile/advanced': getProfileAdvancedData,


if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host="0.0.0.0")