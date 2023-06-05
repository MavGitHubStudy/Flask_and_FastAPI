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
import threading


def get_img_urls(site_url):
    site_text = requests.get(site_url).text
    return set(re.findall('img .*?src="(.*?)"', site_text))


def download(url):
    """Реализация метода по загрузке изображения из url"""
    start_download_file = time.time()
    p = requests.get(url)
    file_name = os.path.basename(url)
    with open(file_name, "wb") as f:
        f.write(p.content)
    print(f'Downloaded {file_name} in {time.time() - start_download_file:2f} seconds')


def main():
    threads = []

    for current_url in urls_for_find:
        img_urls = get_img_urls(current_url)
        for img_url in img_urls:
            if img_url.endswith(".jpg"):
                """Реализация метода по загрузке изображения из img_url"""
                thread = threading.Thread(target=download, args=[img_url])
                threads.append(thread)
                thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    start_prog_time = time.time()

    urls_for_find = [
        'https://gb.ru/',
        'https://github.com',
    ]
    main()
    print(f'Время работы программы: {time.time() - start_prog_time} секунд')
"""
python.exe task_09_thread.py 
Downloaded thumb-4f65b3d56ac4b166033fe2b887accf59.jpg in 0.058006 seconds
Downloaded footer-galaxy.jpg in 0.136014 seconds
Downloaded globe.jpg in 0.148015 seconds
Время работы программы: 0.868086576461792 секунд

Process finished with exit code 0
"""
