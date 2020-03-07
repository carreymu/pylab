from sanic import Sanic
from sanic.response import json, text, html
# from sanic_cors import CORS
import os

app = Sanic('mySanic')
# CORS(app) #跨域

#Serves files from the static folder to the url /static
# app.static('/static','./static')

@app.route('/')
async def test(request):
    return json({'hello': 'world'})

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

@app.route('/post1', methods=['POST'])
async def get_handler(request):
    return json('POST request - {}'.format(request.body))

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

if __name__ == '__main__':
    # open brower and input http://127.0.0.1:8001 in url address
    app.run(host="127.0.0.1", port=8001)

# 