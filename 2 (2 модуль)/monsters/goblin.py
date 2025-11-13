class Goblin:
    def __init__(self):
        self.hp = 1000

    def take_damage(self, dmg):
        self.hp -= dmg
        print(f"Гоблин получает {dmg} урона! HP = {self.hp}")
        if self.hp <= 0:
            print("Гоблин повержен!")