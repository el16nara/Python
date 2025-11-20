class Dragon:
    def __init__(self):
        self.hp = 10000

    def take_damage(self, dmg):
        self.hp -= dmg
        print(f"Дракон получает {dmg} урона! HP = {self.hp}")
        if self.hp <= 0:
            print("Дракон побеждён!")