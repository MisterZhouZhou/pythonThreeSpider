import flask,json

server = flask.Flask(__name__)  # 把当前文件当作服务

@server.route('/index', methods=['get'])
def index():
    res = {'msg': '这个是我开发的第一个接口', 'msg_code': 0}
    return json.dumps(res, ensure_ascii=False)
    # return json.dumps(res, ensure_ascii=False)  # 返回结果是unicode，需要增加ensure_ascii=False

server.run(port=9000, debug=True, host='127.0.0.1')