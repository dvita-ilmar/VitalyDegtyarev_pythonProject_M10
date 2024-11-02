"""
coding: utf-8
Дегтярев Виталий (группа 22/08)
Домашнее задание №10.1
Домашнее задание по теме "Введение в потоки".
"""

import time, datetime, threading


def write_words(word_count, file_name):
    for i in range(word_count):
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(f'Какое-то слово № {i+1}\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

# Запуск
if __name__ == '__main__':

    # получаем время старта
    st = datetime.datetime.now()
    # Вызов функции 4 раза
    write_words(10, 'example1.txt')
    write_words(20, 'example2.txt')
    write_words(200, 'example3.txt')
    write_words(100, 'example4.txt')
    # получаем время завершения
    et = datetime.datetime.now()
    # считаем время исполнения
    elapsed_time = et - st
    print('Время последовательного исполнения функций:', elapsed_time, 'секунд')

    # получаем время старта
    st = datetime.datetime.now()
    # Создание и запуск потоков с аргументами из задачи
    thread1 = threading.Thread(target = write_words, args = (10, 'example5.txt'))
    thread2 = threading.Thread(target = write_words, args = (20, 'example6.txt'))
    thread3 = threading.Thread(target = write_words, args = (200, 'example7.txt'))
    thread4 = threading.Thread(target = write_words, args = (100, 'example8.txt'))

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

    # получаем время завершения
    et = datetime.datetime.now()
    # считаем время исполнения
    elapsed_time = et - st
    print('Время исполнения функций в потоках:', elapsed_time, 'секунд')