from magic.fire import fireball, flame_strike
from magic.ice import ice_shard, frost_nova
from monsters.goblin import Goblin
from monsters.dragon import Dragon
from random import choice
import time

def battle(monster):
    print(f"\nНачинаем бой с {monster.__class__.__name__}!")
    while monster.hp > 0:
        spell = choice([fireball, flame_strike, ice_shard, frost_nova])
        damage = spell()
        monster.take_damage(damage)
        time.sleep(1)

def main():
    goblin = Goblin()
    dragon = Dragon()
    
    battle(goblin)
    battle(dragon)

if __name__ == "__main__":
    main()