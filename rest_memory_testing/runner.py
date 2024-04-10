from docker import DockerClient
from docker.models.containers import Container
from docker.models.images import Image
from os import getenv, getcwd
from pathlib import Path
from collections import defaultdict
from time import sleep
from loguru import logger
from pprint import pformat
from tqdm import tqdm


root_path = Path(getcwd())


client = DockerClient(
    base_url=getenv('DOCKER_BASE_URL')
)


def start_runner():
    memory_usage = defaultdict(list)
    memory_usage_avg = dict()

    for i in ['fastapi', 'quart', 'falcon']:
        logger.debug(f'Build {i}')
        image, logs = client.images.build(
            path=str(root_path),
            tag=f'{i}-memory',
            buildargs={
                'VENDOR': i
            },
            nocache=False
        )
        image: Image
        logger.debug('Start container')
        container: Container = client.containers.run(
            image=image,
            detach=True,
            entrypoint=f'poetry run python ./rest_memory_testing/{i}/app.py',
            name=f'{i}-cont'
        )
        logger.debug("Waiting container to be ready...")
        sleep(15)
        _tqdm = tqdm(desc=i, total=100)
        for _ in range(100):
            _tqdm.update()
            data = container.stats(stream=False)
            memory = data['memory_stats']['usage']
            memory_usage[i].append(memory)
            sleep(.1)
        logger.debug('Down containers and image')
        container.remove(force=True)
        image.remove(force=True)
        memory_usage_avg[i] = sum(memory_usage[i])/100
    logger.debug(memory_usage_avg)
