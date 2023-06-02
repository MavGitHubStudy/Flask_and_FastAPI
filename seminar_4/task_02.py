"""
Задание №2

Написать программу, которая считывает список
из 10 URL-адресов и одновременно загружает
данные с каждого адреса.

После загрузки данных нужно записать их
в отдельные файлы.

Используйте процессы.
"""
import time
import requests
from multiprocessing import Process  # ,Pool

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


def download(_url):
    response = requests.get(_url)
    file_name = 'threading_' + _url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(response.text)
    print(f"Downloaded {_url} in {time.time() - start_time:2f} seconds")


processes = []  # список для наших процессов
start_time = time.time()


if __name__ == '__main__':  # обязательно для процессов!
    for url in urls:
        process = Process(target=download, args=(url, ))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    # for process in processes:
    #     # проверяем, выполняется ли поток в данный момент времени
    #     print(process.is_alive())

"""

Downloaded https://yandex.ru in 0.099010 seconds
Downloaded https://vk.com in 0.376038 seconds
Downloaded https://stepik.org in 0.242024 seconds
Downloaded https://python.org in 0.681068 seconds
Downloaded https://pikabu.ru in 0.274028 seconds
Downloaded https://mail.ru in 0.376038 seconds
Downloaded https://gb.ru/ in 0.542054 seconds
Downloaded https://google.com in 0.774077 seconds
Downloaded https://codelessons.ru in 0.688069 seconds
Downloaded https://yahoo.com in 1.970197 seconds

Process finished with exit code 0

"""
