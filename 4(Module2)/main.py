import pygame
from random import choice, randint
import time

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wizard vs Monsters")

font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

def calculate_damage(base):
    return base

def fireball():
    damage = calculate_damage(randint(100, 200))
    return "Огненный шар", damage

def flame_strike():
    damage = calculate_damage(randint(300, 600))
    return "Огненный удар", damage

def ice_shard():
    damage = calculate_damage(randint(50, 100))
    return "Ледяной осколок", damage

def frost_nova():
    damage = calculate_damage(randint(300, 500))
    return "Ледяное кольцо", damage

class Dragon:
    def __init__(self):
        self.max_hp = 10000
        self.hp = self.max_hp
        self.name = "Дракон"

    def take_damage(self, dmg):
        self.hp -= dmg

class Goblin:
    def __init__(self):
        self.max_hp = 1000
        self.hp = self.max_hp
        self.name = "Гоблин"

    def take_damage(self, dmg):
        self.hp -= dmg

def draw_text(text, x, y):
    render = font.render(text, True, (255, 255, 255))
    screen.blit(render, (x, y))

def draw_hp_bar(monster):
    HP_BAR_WIDTH = 500
    HP_BAR_HEIGHT = 30
    x = 150
    y = 100
    ratio = monster.hp / monster.max_hp
    pygame.draw.rect(screen, (100, 0, 0), (x, y, HP_BAR_WIDTH, HP_BAR_HEIGHT))
    pygame.draw.rect(screen, (255, 0, 0), (x, y, HP_BAR_WIDTH * ratio, HP_BAR_HEIGHT))

def battle(monster):
    running = True
    last_spell = ""
    last_damage = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return False

        screen.fill((20, 20, 20))
        draw_text(f"Бой с: {monster.name}", 300, 40)
        draw_hp_bar(monster)

        if monster.hp > 0:
            spell = choice([fireball, flame_strike, ice_shard, frost_nova])
            spell_name, damage = spell()
            monster.take_damage(damage)
            last_spell = spell_name
            last_damage = damage
            time.sleep(0.5)
        else:
            draw_text("Монстр побеждён!", 300, 300)
            pygame.display.flip()
            time.sleep(2)
            return True

        draw_text(f"{last_spell}: {last_damage} урона", 250, 500)
        pygame.display.flip()
        clock.tick(30)

def main():
    goblin = Goblin()
    dragon = Dragon()
    battle(goblin)
    battle(dragon)
    pygame.quit()

if __name__ == "__main__":
    main()