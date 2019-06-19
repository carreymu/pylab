from sanic import Sanic
from sanic.response import json

app = Sanic()

@app.route('/')
async def test(request):
    return json({'hello': 'world'})


if __name__ == '__main__':
    # open brower and input http://0.0.0.0:8001 in url address
    app.run(host="0.0.0.0", port=8001)

