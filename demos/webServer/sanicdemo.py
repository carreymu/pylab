from sanic import Sanic
from sanic.response import json, text

app = Sanic()

@app.route('/')
async def test(request):
    return json({'hello': 'world'})


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


if __name__ == '__main__':
    # open brower and input http://0.0.0.0:8001 in url address
    app.run(host="0.0.0.0", port=8001)

