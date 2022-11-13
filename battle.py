"""Import all our dependencies"""
import pygame
from pygame import mixer
from hero import Hero
from team import Team
from button import Button
from weapon import Weapon
from armour import Armour
import random

"""Initialize our pygame"""
pygame.init()
mixer.init()

"""All our pygame specific dependencies we need before runtime are here."""
screen = pygame.display.set_mode([2000, 1250])
background = pygame.image.load("Battle-Game-Images/FF4-arena.jpeg").convert_alpha()
all_sprites = pygame.sprite.Group()
attack_button = pygame.image.load("Battle-Game-Images/attack.jpeg").convert_alpha()
clock = pygame.time.Clock()

"""This is currently where we store the heroes. Should creat a file to hold these later if we want to change heroes."""
cecil_harvey = Hero("Battle-Game-Images/Cecil.png", "Cecil Harvey", 3000)
cecil_harvey.add_attack_button(Button(100, 1100, attack_button, 3))
cecil_harvey.add_special_button(Button(100, 1150, attack_button, 3))
cecil_harvey.add_equipment(Weapon("Excalibur", "Sword", 500, 0))
cecil_harvey.add_equipment(Armour("Mithril", 100))

rosa_farrell = Hero("Battle-Game-Images/Rosa-copy.png", "Rosa Farrell", 1800)
rosa_farrell.add_attack_button(Button(500, 1100, attack_button, 3))
rosa_farrell.add_special_button(Button(500, 1150, attack_button, 3))
rosa_farrell.add_equipment(Weapon("Bow", "Bow", 200, 0))
rosa_farrell.add_equipment(Armour("Robe", 50))

edge_geraldin = Hero("Battle-Game-Images/Edge.png", "Edge Geraldin", 2000)
edge_geraldin.add_attack_button(Button(900, 1100, attack_button, 3))
edge_geraldin.add_special_button(Button(900, 1150, attack_button, 3))
edge_geraldin.add_equipment(Weapon("Katana", "Sword", 500, 0))
edge_geraldin.add_equipment(Armour("Gi", 50))

rydia_of_the_mist = Hero("Battle-Game-Images/Rydia-V1-copy.png", "Rydia of the Mist", 1800)
rydia_of_the_mist.add_attack_button(Button(1300, 1100, attack_button, 3))
rydia_of_the_mist.add_special_button(Button(1300, 1150, attack_button, 3))
rydia_of_the_mist.add_equipment(Weapon("Whip", "Whip", 200, 0))
rydia_of_the_mist.add_equipment(Armour("Dress", 50))

kain_highwind = Hero("Battle-Game-Images/Kain-V2-copy.png", "Kain Highwind", 2500)
kain_highwind.add_attack_button(Button(1700, 1100, attack_button, 3))
kain_highwind.add_special_button(Button(1700, 1150, attack_button, 3))
kain_highwind.add_equipment(Weapon("Dragon Lance", "Spear", 500, 0))
kain_highwind.add_equipment(Armour("Dragon Armour", 100))

hero = [cecil_harvey, rosa_farrell, edge_geraldin, rydia_of_the_mist, kain_highwind]

"""Containing teams"""
heroes = Team("Crystal Warriors")
enemies = Team("Baddies")

"""Auto fills our heroes on their team"""
for dude in hero:
    heroes.add_hero(dude)


"""This is to set the position of the hero cards. Could be better if this were lanes the team members got slotted into."""
cecil_harvey.move(0, 600)
rosa_farrell.move(400, 600)
edge_geraldin.move(800, 600)
rydia_of_the_mist.move(1200, 600)
kain_highwind.move(1600, 600)

"""This is the method run to change the song during runtime"""
def play_music(song):
    mixer.music.stop()
    mixer.music.unload()
    mixer.music.load(song)
    mixer.music.play(-1)
    return False

"""All runtime specific variables to maintain operational flow."""
boss_turn = 0
turn = 0
cecil_turn = 0
running = True 
new_battle = True
boss = False
music = True
experience = 0

"""Start the game"""
while running: 
    """This is where we check for exiting the game."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    """Here we set the background image."""
    screen.fill((255, 255, 255))
    screen.blit(background, [0, 0])

    """This is our main Player combat loop, we check for button presses and apply the attack logic."""
    for hero in heroes.heroes:
        if hero.attack_button.draw(screen):
            if len(enemies.heroes) == 0:
                pass
            else:
                enemy = random.choice(enemies.heroes)
                hero.attack(enemy)
                if not enemy.is_alive():
                    enemies.remove_hero(enemy)
                    experience += 500

    """This is to controle the enemy turn cycle to attacking once every 10seconds."""     
    turn += 1
    if turn == 10 * 60:
        for hero in heroes.heroes:
            hero.display_stats()   
        for enemy in enemies.heroes:
            hit_hero = random.choice(heroes.heroes)
            enemy.attack(hit_hero)
            if not hit_hero.is_alive():
                heroes.remove_hero(hit_hero)
        turn = 0
    """Here we render both teams characters onto the screen"""
    for entity in heroes.heroes:
        entity.render(screen)
    for entity in enemies.heroes:
        entity.render(screen)

    """This is how we populate the enemy team between rounds."""
    if new_battle:
        music = play_music("Battle-Game-Music/Fight.mp3")
        number_enemies = random.randint(1, 5)
        while number_enemies > 0:
            enemies.add_hero(Hero("Battle-Game-Images/Goblin-copy.png", "Goblin", 500, 100))
            number_enemies -= 1
        x = 50
        for enemy in enemies.heroes:
            enemy.move(x, 50)
            x += 400
        boss_turn += 1
        new_battle = False
        music = True

    """This is where we check victory conditions and what type of battle the player will face next."""
    if len(enemies.heroes) == 0:
        if music:
            music = play_music("Battle-Game-Music/Fanfare.mp3")
        new_fight_button = Button(1800, 300, attack_button, 4)

        if new_fight_button.draw(screen):
            if boss_turn >= 5:
                boss = True
                new_fight_button = ''
                music = True
            else:
                new_battle = True
                new_fight_button = ''
                music = True

    """Special settings for the boss round."""
    if boss:
        if music:
            music = play_music("Battle-Game-Music/Boss.mp3")
        enemies.add_hero(Hero("Battle-Game-Images/Behemoth-copy.png", "Behemoth", 50000, 500))
        boss = False
        music = True
        for enemy in enemies.heroes:
            enemy.move(700, 50)



    """This is where we set the game refresh rate and tell the game to refresh."""
    pygame.display.flip()
    clock.tick(60)
