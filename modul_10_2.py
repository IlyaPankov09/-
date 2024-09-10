from threading import Thread
from time import sleep

class Knight(Thread):

    def __init__(self, name = str, power = int):
        self.name = name
        self.power = power
        super().__init__()

    def run(self):
        print(f'{self.name}, на нас напали!')
        life = 100
        days = 0
        while life > 0:
            sleep(1)
            days += 1
            life -= self.power
            if life < 0:
                life = 0
            print(f'{self.name} сражается {days} суток, осталось {life} воинов врага.')
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')
def main():
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)

    first_knight.start()
    second_knight.start()
    first_knight.join()
    second_knight.join()

    print('Все битвы закончились')

if __name__ == '__main__':
    main()

