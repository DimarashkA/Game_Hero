import random
from tqdm import tqdm
from colorama import Fore, Style, init

init(autoreset=True)

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        if self.is_alive():
            damage = random.randint(10, self.attack_power)
            other.health -= damage
            print(f"\n{Fore.RED}{self.name} атакует {other.name} и отнимает {damage} здоровья.")
            self.display_health_bar()
            other.display_health_bar()
            self.visualize_attack(other)
        else:
            print(f"\n{Fore.RED}{self.name} не может атаковать, так как он мертв.")

    def is_alive(self):
        return self.health > 0

    def visualize_attack(self, other):
        print(f"{self.name} ---> {Fore.YELLOW}*БОЙ*{Style.RESET_ALL} <--- {other.name}")

    def display_health_bar(self):
        progress = tqdm(total=100, position=0, leave=True, bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}')
        progress.n = self.health
        progress.set_description(f"{self.name}")
        progress.refresh()


class Game:
    def __init__(self):
        player_name = input("Введите имя вашего героя: ")
        self.player = Hero(player_name)
        self.computer = Hero("Компьютерный Герой")

    def start(self):
        print("\nБитва начинается!")
        self.player.display_health_bar()
        self.computer.display_health_bar()

        while self.player.is_alive() and self.computer.is_alive():
            self.player.attack(self.computer)
            if not self.computer.is_alive():
                print(f"\n{Fore.GREEN}{self.player.name} победил!")
                break

            input("\nНажмите Enter, чтобы продолжить бой...")

            self.computer.attack(self.player)
            if not self.player.is_alive():
                print(f"\n{Fore.RED}{self.computer.name} победил!")
                break

            input("\nНажмите Enter, чтобы продолжить бой...")

        print("\nИгра окончена.")


if __name__ == "__main__":
    game = Game()
    game.start()