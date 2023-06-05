"""
Задание №9

Написать программу, которая считывает изображения
с заданных URL-адресов и сохраняет их на диск. Каждое
изображение должно сохраняться в отдельном файле,
название которого соответствует названию изображения
в URL-адресе.

Например, URL-адрес: https://example/images/image1.jpg->
файл на диске: image1.jpg

Программа должна использовать многопоточный,
многопроцессорный и асинхронный подходы.

Программа должна иметь возможность задавать список
URL-адресов через аргументы командной строки.

Программа должна выводить в консоль информацию
о времени скачивания каждого изображения и общем
времени выполнения программы.
"""
import time
import re
import requests
import os
import asyncio
import aiohttp
import aiofiles


def get_img_urls(site_url):
    site_text = requests.get(site_url).text
    return set(re.findall('img .*?src="(.*?)"', site_text))


async def download(url):
    """Реализация метода по загрузке изображения из url"""
    start_download_file = time.time()
    async with aiohttp.ClientSession() as session:
        file_name = os.path.basename(url)
        async with session.get(url) as resp:
            if resp.status == 200:
                async with aiofiles.open(file_name, "wb") as f:
                    await f.write(await resp.read())

    print(f'Downloaded {file_name} in {time.time() - start_download_file:2f} seconds')


async def main():
    tasks = []

    for current_url in urls_for_find:
        img_urls = get_img_urls(current_url)
        for img_url in img_urls:
            if img_url.endswith(".jpg"):
                """Реализация метода по загрузке изображения из img_url"""
                task = asyncio.ensure_future(download(img_url))
                tasks.append(task)

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    start_prog_time = time.time()

    urls_for_find = [
        'https://gb.ru/',
        'https://github.com',
    ]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

    print(f'Время работы программы: {time.time() - start_prog_time} секунд')
"""
python.exe task_09_process.py 
Downloaded thumb-4f65b3d56ac4b166033fe2b887accf59.jpg in 0.058006 seconds
Downloaded footer-galaxy.jpg in 0.125012 seconds
Downloaded globe.jpg in 0.136014 seconds
Время работы программы: 0.9730973243713379 секунд

Process finished with exit code 0
"""
