# Million Dogs

Два способа загрузить 100 фотографий собак: последовательно и асинхронно.

**Python · requests · aiohttp · aiofiles**

## Быстрый старт

```bash
git clone https://github.com/KobaLuck/million_dogs.git
cd million_dogs
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python download_dog.py
# Асинхронная версия:
python async_download_dogs.py
```

В Windows PowerShell окружение активируется командой `.venv\Scripts\Activate.ps1`.

Изображения сохраняются в `dogs/` рядом со скриптами. Для работы нужен доступ к TheDogAPI и серверам изображений.

## Структура

- `async_download_dogs.py` — исходный код.
- `download_dog.py` — исходный код.

---

[Никита Казанцев](https://github.com/KobaLuck) · [Все публичные проекты](https://github.com/KobaLuck?tab=repositories)
