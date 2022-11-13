from arena import Arena
import pygame
from pygame import mixer
from hero import Hero
from team import Team
from button import Button
from weapon import Weapon
from armour import Armour
import random
clock = pygame.time.Clock()

pygame.init()
mixer.init()

# mixer.music.set_volume(1)
screen = pygame.display.set_mode([2000, 1250])
background = pygame.image.load("Battle-Game-Images/FF4-arena.jpeg").convert_alpha()
all_sprites = pygame.sprite.Group()
attack_button = pygame.image.load("Battle-Game-Images/attack.jpeg").convert_alpha()


cecil_harvey = Hero("Battle-Game-Images/Cecil.png", "Cecil Harvey", 3000)
cecil_harvey.add_button(Button(100, 1100, attack_button, 3))
cecil_harvey.add_equipment(Weapon("Excalibur", "Sword", 500, 0))
cecil_harvey.add_equipment(Armour("Mithril", 100))

rosa_farrell = Hero("Battle-Game-Images/Rosa-copy.png", "Rosa Farrell", 1800)
rosa_farrell.add_button(Button(500, 1100, attack_button, 3))
rosa_farrell.add_equipment(Weapon("Bow", "Bow", 200, 0))
rosa_farrell.add_equipment(Armour("Robe", 50))

edge_geraldin = Hero("Battle-Game-Images/Edge.png", "Edge Geraldin", 2000)
edge_geraldin.add_button(Button(900, 1100, attack_button, 3))
edge_geraldin.add_equipment(Weapon("Katana", "Sword", 500, 0))
edge_geraldin.add_equipment(Armour("Gi", 50))

rydia_of_the_mist = Hero("Battle-Game-Images/Rydia-V1-copy.png", "Rydia of the Mist", 1800)
rydia_of_the_mist.add_button(Button(1300, 1100, attack_button, 3))
rydia_of_the_mist.add_equipment(Weapon("Whip", "Whip", 200, 0))
rydia_of_the_mist.add_equipment(Armour("Dress", 50))

kain_highwind = Hero("Battle-Game-Images/Kain-V2-copy.png", "Kain Highwind", 2500)
kain_highwind.add_button(Button(1700, 1100, attack_button, 3))
kain_highwind.add_equipment(Weapon("Dragon Lance", "Spear", 500, 0))
kain_highwind.add_equipment(Armour("Dragon Armour", 100))

hero = [cecil_harvey, rosa_farrell, edge_geraldin, rydia_of_the_mist, kain_highwind]

heroes = Team("Crystal Warriors")
enemies = Team("Baddies")

for dude in hero:
    heroes.add_hero(dude)

cecil_harvey.move(0, 600)
rosa_farrell.move(400, 600)
edge_geraldin.move(800, 600)
rydia_of_the_mist.move(1200, 600)
kain_highwind.move(1600, 600)

boss_turn = 0
turn = 0
cecil_turn = 0
running = True 
new_battle = True
boss = False
music = True
experience = 0
while running: 
	# Looks at events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255))
    screen.blit(background, [0, 0])


    for hero in heroes.heroes:
        if hero.button.draw(screen):
            enemy = random.choice(enemies.heroes)
            hero.attack(enemy)
            if not enemy.is_alive():
                enemies.remove_hero(enemy)
                experience += 500
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

    for entity in heroes.heroes:
        entity.render(screen)
    for entity in enemies.heroes:
        entity.render(screen)

    if new_battle:
        mixer.music.unload()
        mixer.music.load("Battle-Game-Music/Fight.mp3")
        mixer.music.play(-1)
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

    # VIctory condition
    if len(enemies.heroes) == 0:
        if music:
            mixer.music.stop()
            mixer.music.unload()
            mixer.music.load("Battle-Game-Music/Fanfare.mp3")
            mixer.music.play(-1)
            music = False
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


    if boss:
        if music:
            mixer.music.unload()
            mixer.music.load("Battle-Game-Music/Boss.mp3")
            mixer.music.play(-1)
            music = False
        enemies.add_hero(Hero("Battle-Game-Images/Behemoth-copy.png", "Behemoth", 50000, 500))
        boss = False
        music = True
        for enemy in enemies.heroes:
            enemy.move(700, 50)



    # Update the display
    pygame.display.flip()
    clock.tick(60)
