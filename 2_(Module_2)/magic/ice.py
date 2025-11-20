from random import randint
from .utils import calculate_damage

def ice_shard():
    damage = calculate_damage(randint(50,100))
    print(f"Ледяной осколок {damage} урона!")
    return damage

def frost_nova():
    damage = calculate_damage(randint(300,500))
    print(f"Ледяной кольцо {damage} урона!")
    return damage