from random import randint
from .utils import calculate_damage

def fireball():
    damage = calculate_damage(randint(100,200))
    print(f"Огненный шар наносит {damage} урона!")
    return damage

def flame_strike():
    damage = calculate_damage(randint(300,600))
    print(f"Огненный удар наносит {damage} урона!")
    return damage