import asyncio
import importlib.util
from pathlib import Path
from unittest.mock import AsyncMock, patch

def module(name):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).parents[1] / (name+'.py'))
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value

def test_async_download_writes_bytes(tmp_path):
    downloader = module('async_download_dogs')
    downloader.DOGS_DIR = tmp_path
    response = AsyncMock()
    response.read.return_value = b'image-bytes'
    response.raise_for_status = lambda: None
    session = AsyncMock()
    session.get.return_value = response
    with patch.object(downloader.aiohttp, 'ClientSession') as factory:
        factory.return_value.__aenter__.return_value = session
        asyncio.run(downloader.download_file('https://example.com/dog.jpg'))
    assert (tmp_path/'dog.jpg').read_bytes() == b'image-bytes'

def test_main_creates_directory_beside_script(tmp_path):
    downloader = module('async_download_dogs')
    downloader.DOGS_DIR = tmp_path/'pictures'
    with patch.object(downloader, 'download_new_dog_image', new_callable=AsyncMock) as download:
        asyncio.run(downloader.main())
    assert downloader.DOGS_DIR.is_dir()
    assert download.await_count == 100
