from quart import Quart

app = Quart(__name__)


@app.get('/')
async def index():
    return {
        'message': "Hello world!"
    }


def run() -> None:
    app.run(host='0.0.0.0', port=7197)

if __name__ == '__main__':
    run()
