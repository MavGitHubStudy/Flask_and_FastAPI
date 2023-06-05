"""
Задание №7

Напишите программу на Python, которая будет находить
сумму элементов массива из 1000000 целых чисел.

Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,...]

Массив должен быть заполнен случайными числами
от 1 до 100.

Вывести время выполнения вычислений.

При решении задачи использовать многопроцессорность.
"""
import time
from multiprocessing import Process
from random import randint

arr = []
arr_size = 1_000_000


def fill_arr():
    global arr

    filling_start = time.time()
    for _ in range(1, arr_size + 1):
        arr.append(randint(1, 100))
    filling_time = time.time() - filling_start
    print(f"Время заполнения массива: {filling_time}")
    # print(arr[0:20])


def summing_arr_elements():
    global arr

    summation_start = time.time()
    sum_of_arr = sum(arr)
    summation_time = time.time() - summation_start
    print(f"Время суммирования элементов массива: {summation_time}")
    print(f"Сумма элементов массива: {sum_of_arr}")


def main():
    processes = []

    # Process created for fill
    p1 = Process(target=fill_arr())
    # Process created for summing
    p2 = Process(target=summing_arr_elements())

    processes.append(p1)
    p1.start()
    processes.append(p2)
    p2.start()

    for process in processes:
        process.join()


if __name__ == '__main__':
    main()
