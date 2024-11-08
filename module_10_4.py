"""
coding: utf-8
Дегтярев Виталий (группа 22/08)
Домашнее задание №10.4
Домашнее задание по теме "Очереди для обмена данными между потоками."
"""


import time, random, threading
from queue import Queue

# Столы
class Table:

    def __init__(self, number):
        self.number = number
        self.guest = None

# Гости
class Guest(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10)) # Процесс обслуживания гостя

# Кафе
class Cafe:

    def __init__(self, *tables):
        self.tables = list(tables)
        self.queue = Queue()

    # Посадка гостей за свободные столы или постановка их в очередь
    def guest_arrival(self, *guests):
        free_table_counter = len(tables) #Счетчик свободных столов
        for guest in guests:
            for table in tables:
                if table.guest is None:  # Рассадка гостей за свободные столы
                    table.guest = guest
                    free_table_counter -= 1
                    guest.start() # Гость начинает обслуживаться
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    break
                else:
                    if free_table_counter == 0: # Если свободных столов не осталось
                        self.queue.put(guest) # Постановка гостей в очередь
                        print(f'{guest.name} в очереди')
                        break

    # Обслуживание гостей (Не чистый метод - работает с внешними данными напрямую, ну так оно по условию задачи...)
    def discuss_guests(self):
        occupied_table_counter = len(tables) # Счетчик занятых столов
        empty_hall = False # Флаг пустого зала
        while not (self.queue.empty() and empty_hall):
            for table in tables:
                if not table.guest is None: # Если стол не пуст - только тогда можно проверить что там кто-то есть или был
                    if not table.guest.is_alive(): # Если гость ушел
                        print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                        print(f'Стол номер {table.number} свободен')
                        table.guest = None # Стол помечается как пустой
                        if not self.queue.empty(): # Если очередь не пуста
                            table.guest = self.queue.get() # Садим за стол нового гостя
                            print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                            table.guest.start() # Новый гость начинает обслуживаться
                        else:
                            occupied_table_counter -= 1 # На один освободившийся стол становится больше
                            if occupied_table_counter == 0: # Если все столы освободились
                                empty_hall = True # Кафе опустело и закрывается
                                print('Кафе опустело и закрывается')


# Запуск
if __name__ == '__main__':
    # Создание столов
    tables = [Table(number) for number in range(1, 6)]
    # Имена гостей
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]
    # Создание гостей
    guests = [Guest(name) for name in guests_names]
    # Заполнение кафе столами
    cafe = Cafe(*tables)
    # Приём гостей
    cafe.guest_arrival(*guests)
    # Обслуживание гостей
    cafe.discuss_guests()