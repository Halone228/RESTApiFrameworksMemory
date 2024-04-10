from fastapi import FastAPI
from uvicorn import run as uvicorn_run

app = FastAPI()


@app.get('/')
async def index():
    return {
        'message': 'Hello world!'
    }


def run() -> None:
    uvicorn_run(app, host='0.0.0.0', port=7198)


if __name__ == '__main__':
    run()