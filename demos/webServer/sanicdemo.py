from sanic import Sanic
from sanic.response import json, text, html, stream
from sanic import response
# from sanic_cors import CORS
from sanic.blueprints import Blueprint
from sanic.exceptions import ServerError
from sanic.views import HTTPMethodView
import asyncio
import time
import os


app = Sanic(__name__)
# app = Sanic('mySanic', strict_slashes=True)
# CORS(app) #Cross-domain

#Serves files from the static folder to the url /static
# app.static('/static','./static')
# app.static('/uploads', './uploads', name='uploads')
# app.static('/the_best.png', '/home/ubuntu/test.png', name='best_png')


@app.route('/')
async def test(request):
    # print( response.text(request['foo']))
    return json({'hello': 'world','foo':request['foo']}) #curl 127.0.0.1:8001

@app.route('/', version=1)
async def test(request):
    return json({'hello': 'world','version':'v1'}) #curl 127.0.0.1:8001/v1

@app.route('/', version=2)
async def test(request):
    return json({'hello': 'world','version':'v2'}) #curl 127.0.0.1:8001/v1

@app.route('/html')
async def load_html(request):
    template = open(os.getcwd()+"/templates/index.html").read()
    return html(template)

@app.get('/ping')
async def hs(request):
    return text('resposne - pong')

@app.route('/tag/<tag>')
async def tag_handler(request, tag):
    return text('Tag-{}'.format(tag))


@app.route('/number/<integer_arg:int>')
async def integer_handler(request, integer_arg):
    return text('Integer - {}'.format(integer_arg))


@app.route('/person/<name:[A-z]>')
async def person_handler(request, name):
    return text('Person - {}'.format(name))


@app.route('/folder/<folder_id:[A-Za-z0-9]{4,40}')
async def folder_handler(request, folder_id):
    print('ddd')
    return text('Folder-{}'.format(folder_id))


@app.route('/json', methods=['POST'])
async def post_json(request):
    print(request.json)
    return text("it is ok!")
    # return json({"received": request.json})

@app.get('/shortget', name='gets_handler')
async def get_handler(request):
    return text('GET request - {}'.format(request.args))
# 当为上面的路由使用`url_for`时，
# 应该使用 `app.url_for('gets_handler')`
# 而不是`app.url_for('get_handler')`

@app.route('/post', methods=['POST'], host='www.baidu.com')
async def post_handler(request):
    return response.text('POST request: {}'.format(request.json))

@app.post('/shortpost')
async def post_handler(request):
    return text('POST request - {}'.format(request.json))

@app.route('/many', methods=['GET', 'POST', 'DELETE'])
async def many_handler(request):
    return response.text('many request: {}'.format(request.json))

@app.route('/args')
async def test(request):
    return json({
        "parsed": True,
        "url": request.url,
        "query_string": request.query_string,
        "args": request.args,
        "raw_args": request.raw_args,
        # "query_args": request.query_args,
    })

@app.route("/files", methods=['POST'])
async def post_json(request):
    test_file = request.files.get('file1')
    file_parameters = {
        'body': len(test_file.body),
        'name': test_file.name,
        'type': test_file.type,
    }

    return json({
        "received": True,
        "file_object_names": request.files.keys(),
        "test_file_parameters": file_parameters
    })

@app.route('/stream')
async def streaming(request):
    async def streaming_fn(response):
        await response.write('Welcom to @{}\n'.format(time.strftime('%H:%M:%S')))
        await asyncio.sleep(3)
        await response.write('Hello Python @{}\n'.format(time.strftime('%H:%M:%S')))
    return stream(
        streaming_fn,
        headers={'X-Serverd-By': 'Hello Python'}
    )

#####################listener#########################
@app.listener('before_server_start')
async def setup_db(app, loop):
    print('Server successfully before_server_start!')

@app.listener('after_server_start')
async def notify_server_started(app, loop):
    print('Server successfully started!')

@app.listener('before_server_stop')
async def notify_server_stopping(app, loop):
    print('Server shutting down!')

@app.listener('after_server_stop')
async def close_db(app, loop):
    print('Server successfully after_server_stop!')

async def notify_server_started_after_five_seconds():
    await asyncio.sleep(5)
    print('Server successfully sleeps 5s!')
#####################middleware#########################
@app.middleware('request')
async def add_key(request):
    request['foo'] = 'bar'

@app.middleware('response')
async def custom_banner(request, response):
    response.headers["Server"] = "Fake-Serverss"

#####################Blueprint,Global version controller#########################
# bp = Blueprint('my_blueprint')
# @bp.route('/')
# async def bp_root(request):
#     return json({'my': 'blueprint'})

#####################Error#########################
@app.route('/killme')
async def i_am_ready_to_die(request):
    raise ServerError("Something bad happened", status_code=500)


class SimpleAsyncView(HTTPMethodView):
#   @staticmethod
  async def get(self, request, name):
        return text('I am async get method, hello {}'.format(name))
  async def post(self, request, name):
        return text('I am async post method, hello {}'.format(name))
  def put(self, request):
        return text('I am put method')
if __name__ == '__main__':
    app.add_route(SimpleAsyncView.as_view(), '/view/<name>')
    app.add_task(notify_server_started_after_five_seconds())
    # open brower and input http://127.0.0.1:8001 in url address
    app.run(host="127.0.0.1", port=8001) #, debug=True
    
# 