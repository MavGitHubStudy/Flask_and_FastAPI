"""
Задание №7

Напишите программу на Python, которая будет находить
сумму элементов массива из 1000000 целых чисел.

Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,...]

Массив должен быть заполнен случайными числами
от 1 до 100.

Вывести время выполнения вычислений.

При решении задачи использовать многопоточность.
"""
import time
import threading
from random import randint

arr = []
arr_size = 1_000_000


def fill_arr():
    global arr
    global lock

    filling_start = time.time()
    with lock:
        for _ in range(1, arr_size + 1):
            arr.append(randint(1, 100))

    filling_time = time.time() - filling_start
    print(f"Время заполнения массива: {filling_time}")
    # print(arr[0:20])


def summing_arr_elements():
    global arr
    global lock

    summation_start = time.time()
    # Here the array is being synchronized
    with lock:
        sum_of_arr = sum(arr)

    summation_time = time.time() - summation_start
    print(f"Время суммирования элементов массива: {summation_time}")
    print(f"Сумма элементов массива: {sum_of_arr}")
    return sum_of_arr


def main():
    threads = []

    # Thread created for fill
    t1 = threading.Thread(target=lambda: fill_arr())

    # Thread created for summing
    t2 = threading.Thread(target=lambda: summing_arr_elements())

    threads.append(t1)
    t1.start()
    threads.append(t2)
    t2.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    # Lock object to synchronize access to the array
    lock = threading.Lock()

    main()
