from flask import Flask, jsonify, redirect, request

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
    print()
    app.run(debug=True)