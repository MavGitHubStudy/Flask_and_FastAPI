"""
Задание №1

Написать программу, которая считывает список
из 10 URL-адресов и одновременно загружает
данные с каждого адреса.

После загрузки данных нужно записать их
в отдельные файлы.

Используйте потоки.
"""
import threading
import time
import requests

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

threads = []  # список для наших потоков
start_time = time.time()


def download(_url):
    response = requests.get(_url)
    file_name = 'threading_' + _url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(response.text)
    print(f"Downloaded {_url} in {time.time() - start_time:2f} seconds")


for url in urls:
    thread = threading.Thread(target=download, args=[url])
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

# for thread in threads:
#     # проверяем, выполняется ли поток в данный момент времени
#     print(thread.is_alive())

"""

Downloaded https://yandex.ru in 0.136014 seconds
Downloaded https://stepik.org in 0.300030 seconds
Downloaded https://gb.ru/ in 0.398040 seconds
Downloaded https://mail.ru in 0.426042 seconds
Downloaded https://pikabu.ru in 0.600060 seconds
Downloaded https://vk.com in 1.054105 seconds
Downloaded https://python.org in 1.123112 seconds
Downloaded https://google.com in 1.337134 seconds
Downloaded https://codelessons.ru in 1.549155 seconds
Downloaded https://yahoo.com in 1.620162 seconds

Process finished with exit code 0

"""
