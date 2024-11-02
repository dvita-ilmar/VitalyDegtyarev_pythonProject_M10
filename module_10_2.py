"""
coding: utf-8
Дегтярев Виталий (группа 22/08)
Домашнее задание №10.2
Домашнее задание по теме "Потоки на классах"
"""


import time, threading


class Knight(threading.Thread):

    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name}, на нас напали!")
        warriors = 100 # Количество войнов
        days = int(100 / self.power) # Количество дней сражения
        for i in range(days):
            time.sleep(1)
            warriors -= self.power
            print(f"{self.name} сражается {i} день(дня), осталось {warriors} воинов.")
        print(f"{self.name} одержал победу спустя {days} дней(дня)!")


# Запуск
if __name__ == '__main__':

    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight('Sir Galahad', 20)

    first_knight.start()
    second_knight.start()

    first_knight.join()
    second_knight.join()

    print('Все битвы закончились!')