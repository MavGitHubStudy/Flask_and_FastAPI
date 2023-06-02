"""
Задание №3

Написать программу, которая считывает список
из 10 URL-адресов и одновременно загружает
данные с каждого адреса.

После загрузки данных нужно записать их
в отдельные файлы.

Используйте асинхронный подход.
"""
import asyncio
import aiohttp
import time


urls = [
    'https://gb.ru/',
    'https://google.com',
    'https://yandex.ru',
    'https://python.org',
    'https://mail.ru',
    'https://stepik.org',
    'https://vk.com',
    'https://yahoo.com',
    'https://pikabu.ru',
    'https://codelessons.ru'
    ]


async def download(_url):
    async with aiohttp.ClientSession() as session:
        async with session.get(_url) as response:
            text = await response.text()
            file_name = 'asyncio_' + _url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"Downloaded {_url} in {time.time() - start_time:2f} seconds")


async def main():
    tasks = []
    for _url in urls:
        task = asyncio.ensure_future(download(_url))
        tasks.append(task)
    await asyncio.gather(*tasks)

start_time = time.time()

if __name__ == '__main__':  # обязательно для асинхронного подхода!
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

"""

Downloaded https://yandex.ru in 0.123012 seconds
Downloaded https://vk.com in 0.275028 seconds
Downloaded https://gb.ru/ in 0.418042 seconds
Downloaded https://mail.ru in 0.428043 seconds
Downloaded https://python.org in 0.443044 seconds
Downloaded https://stepik.org in 0.488049 seconds
Downloaded https://pikabu.ru in 0.591059 seconds
Downloaded https://codelessons.ru in 0.709071 seconds
Downloaded https://google.com in 0.809081 seconds
Downloaded https://yahoo.com in 1.293129 seconds

Process finished with exit code 0

"""
