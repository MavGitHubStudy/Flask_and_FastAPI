"""
Задание №7

Напишите программу на Python, которая будет находить
сумму элементов массива из 1000000 целых чисел.

Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,...]

Массив должен быть заполнен случайными числами
от 1 до 100.

Вывести время выполнения вычислений.

При решении задачи использовать асинхронность.
"""
import time
import asyncio
from random import randint

arr = []
arr_size = 1_000_000


async def fill_arr():
    global arr

    filling_start = time.time()
    for _ in range(1, arr_size + 1):
        arr.append(randint(1, 100))

    filling_time = time.time() - filling_start
    print(f"Время заполнения массива: {filling_time}")
    # print(arr[0:20])


async def summing_arr_elements():
    global arr

    summation_start = time.time()
    sum_of_arr = sum(arr)

    summation_time = time.time() - summation_start
    print(f"Сумма элементов массива: {sum_of_arr}")
    print(f"Время выполнения вычислений: {summation_time}")
    return sum_of_arr


async def main():
    tasks = []

    task1 = asyncio.ensure_future(fill_arr())
    task2 = asyncio.ensure_future(summing_arr_elements())
    tasks.append(task1)
    tasks.append(task2)
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
