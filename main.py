# Создайте простую текстовую боевую игру, где игрок и компьютер управляют героями с различными характеристиками. Игра состоит из раундов, в каждом раунде игроки по очереди наносят урон друг другу, пока у одного из героев не закончится здоровье.
# Требования:
# 1.	Используйте ООП (Объектно-Ориентированное Программирование) для создания
# классов героев.
# 2.	Игра должна быть реализована как консольное приложение.
# Классы:
# Класс Hero:
# •	Атрибуты:
# •	Имя (name)
# •	Здоровье (health), начальное значение 100
# •	Сила удара (attack_power), начальное значение 20
# •	Методы:
# •	attack(other): атакует другого героя (other), отнимая здоровье в размере
# своей силы удара
# •	is_alive(): возвращает True, если здоровье героя больше 0, иначе False
# Класс Game:
# •	Атрибуты:
# •	Игрок (player), экземпляр класса Hero
# •	Компьютер (computer), экземпляр класса Hero
# •	Методы:
# •	start(): начинает игру, чередует ходы игрока и компьютера, пока один из
# героев не умрет. Выводит информацию о каждом ходе (кто атаковал и сколько
# здоровья осталось у противника) и объявляет победителя.



class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 40

    def attac(self, other):
        other.health -= self.attack_power
    def is_alive(self):
         return self.health > 0

class Game:
    def __init__(self, player):
        self.player = Hero(player)
        self.computer = Hero("Компьютер")

    def start(self):
        print("Игра началась!")
        while self.player.is_alive() and self.computer.is_alive():
            print("_________________________")
            print(f"{self.player.name} атакует!")
            self.player.attac(self.computer)

            if not self.computer.is_alive():
                print(f"Побеждает {self.player.name}")
                break

            print(f"{self.computer.name} - здоровье: {self.computer.health} ")
            print(f"{self.player.name} - здоровье: {self.player.health} ")

            print("_________________________")
            print(f"{self.computer.name} атакует!")
            self.computer.attac(self.player)

            if not self.player.is_alive():
                print(f"Побеждает {self.computer.name} ")
                break

            print(f"{self.computer.name} - здоровье: {self.computer.health} ")
            print(f"{self.player.name} - здоровье: {self.player.health} ")


game = Game("Герой")
game.start()


