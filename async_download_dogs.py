from datetime import datetime
from pathlib import Path
import asyncio

import aiofiles
import aiohttp
import aiofiles.os

URL = 'https://api.thedogapi.com/v1/images/search'
BASE_DIR = Path(__file__).parent
DOGS_DIR = BASE_DIR / 'dogs'


async def get_new_image_url():
    async with aiohttp.ClientSession() as session:
        response = await session.get(URL)
        data = await response.json()
        random_dog = data[0]['url']
        return random_dog


async def download_file(url):
    file_name = url.split('/')[-1]
    async with aiohttp.ClientSession() as session:
        result = await session.get(url)
        async with aiofiles.open(DOGS_DIR / file_name, 'wb') as f:
            f.write(await result.read())


async def download_new_dog_image():
    url = await get_new_image_url()
    await download_file(url)


async def create_dir(dir_name):
    await aiofiles.os.makedirs(dir_name, exist_ok=True)


async def list_dir(dir_name):
    files_and_dirs = await aiofiles.os.listdir(dir_name)
    print(*files_and_dirs, sep='\n')


async def main():
    await create_dir('dogs')
    tasks = [
        asyncio.ensure_future(download_new_dog_image()) for _ in range(100)
    ]

    await asyncio.wait(tasks)

if __name__ == '__main__':
    start_time = datetime.now()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    asyncio.run(list_dir(DOGS_DIR))

    end_time = datetime.now()
    print(f'Время выполнения программы: {end_time - start_time}.')
