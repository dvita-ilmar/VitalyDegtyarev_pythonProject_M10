"""
coding: utf-8
Дегтярев Виталий (группа 22/08)
Домашнее задание №10.5
Домашнее задание по теме "Многопроцессное программирование"
"""


import datetime
from multiprocessing import Pool


def read_info(name):
    all_data = [] # Инициализация списка записи строк
    with open(name, encoding='utf-8') as file:
        while True:
            # считываем строку
            line = file.readline()
            # прерываем цикл, если строка пустая
            if not line:
                break
            # Записываем строку
            all_data.append(line)


# Запуск
if __name__ == '__main__':

    filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
    # получаем время старта
    st = datetime.datetime.now()

    for filename in filenames: read_info(filename)

    # получаем время завершения
    et = datetime.datetime.now()
    # считаем время исполнения
    elapsed_time = et - st
    print('Время исполнения:', elapsed_time, 'секунд')  # Время исполнения: 0:00:06.450960 секунд (у меня)

# Многопроцессный вызов
    st = datetime.datetime.now()
    with Pool(4) as p:
        p.map(read_info, filenames)
    et = datetime.datetime.now()
    elapsed_time = et - st
    print('Время исполнения:', elapsed_time, 'секунд')  # Время исполнения: 0:00:02.994795 секунд (у меня)