import asyncio
from pathlib import Path


async def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        contents = f.read()
        # do some processing with the file contents
        # печатаем имя файла и его первые 13 символов
        print(f'{f.name} содержит <<<{contents[:13]})...>>>')


async def main():
    # dir_path = Path('/path/to/directory')
    dir_path = Path('.')  # текущий каталог lesson_4
    file_paths = [file_path for file_path in dir_path.iterdir() if file_path.is_file()]
    # для каждого файла создай свою корутину и все
    # эти корутины запусти в виде асинхронного кода
    tasks = [asyncio.create_task(process_file(file_path)) for file_path in file_paths]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
