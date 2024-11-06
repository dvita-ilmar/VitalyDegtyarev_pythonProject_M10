"""
coding: utf-8
Дегтярев Виталий (группа 22/08)
Домашнее задание №10.3
Домашнее задание по теме "Блокировки и обработка ошибок"
"""


import time, random, threading


class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock() # Инициализация замка

    def deposit(self):
        for transact in range(100):
            depo = random.randint(50, 500) # Сумма, предложенная к пополнению депозита
            self.balance += depo #  Пополнение депозита
            print(f"Пополнение: {depo}. Баланс: {self.balance}")
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)

    def take(self):
           for transact in range(100):
                repo = random.randint(50, 500) # Сумма, предложенная к снятию с депозита
                print(f"Запрос на снятие {repo}$. Баланс {self.balance}$")
                if self.balance >= repo:
                    self.balance -= repo  # Снятие с депозита
                    print(f"Снятие: {repo}$. Баланс: {self.balance}$")
                else:
                    print("Запрос отклонён, недостаточно средств")
                    self.lock.acquire()


# Запуск
if __name__ == '__main__':
    bk = Bank()

    th1 = threading.Thread(target=Bank.deposit, args=(bk,))
    th2 = threading.Thread(target=Bank.take, args=(bk,))

    th1.start()
    th2.start()
    th1.join()
    th2.join()

    print(f'Итоговый баланс: {bk.balance}')