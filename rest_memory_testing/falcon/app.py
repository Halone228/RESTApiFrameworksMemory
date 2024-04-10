from falcon.asgi import App, Request, Response
from falcon import HTTP_200, MEDIA_JSON
from uvicorn import run as uvicorn_run


class IndexResource:
    async def on_get(self, req: Request, resp: Response):
        resp.status = HTTP_200
        resp.content_type = MEDIA_JSON
        resp.text = {
            'message': 'Hello world!'
        }


app = App()
app.add_route('/', IndexResource())


def run() -> None:
    uvicorn_run(app, host='0.0.0.0', port=7199)


if __name__ == '__main__':
    run()