from arena import Arena
import pygame
from hero import Hero
from team import Team
import random
clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode([2000, 1250])
all_sprites = pygame.sprite.Group()


cecil_harvey = Hero("Battle-Game-Images/Cecil.png", "Cecil", 3000)
rosa_farrell = Hero("Battle-Game-Images/Rosa-copy.jpg", "Rosa", 1800)
edge_geraldin = Hero("Battle-Game-Images/Edge.png", "Edge", 2000)
rydia_of_the_mist = Hero("Battle-Game-Images/Rydia-V1-copy.jpg", "Rydia", 1800)
kain_highwind = Hero("Battle-Game-Images/Kain-V2-copy.jpg", "Kain", 2500)

goblin = Hero("Battle-Game-Images/Goblin-copy.jpg", "Goblin", 500)
behemoth = Hero("Battle-Game-Images/Behemoth-copy.jpg", "Behemoth", 50000)


hero = [cecil_harvey, rosa_farrell, edge_geraldin, rydia_of_the_mist, kain_highwind]


heroes = Team("Crystal Warriors")
enemies = Team("Baddies")

for dude in hero:
    heroes.add_hero(dude)



cecil_harvey.move(0, 600)
rosa_farrell.move(400, 600)
behemoth.move(700, 50)
edge_geraldin.move(800, 600)
rydia_of_the_mist.move(1200, 600)
kain_highwind.move(1600, 600)


cecil_turn = 0
running = True 
while running: 
	# Looks at events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255))

    for entity in hero:
        entity.render(screen)
    for entity in enemies.heroes:
        entity.render(screen)

    if len(enemies.heroes) == 0:
        number_enemies = random.randint(1, 5)
        while number_enemies > 0:
            enemies.add_hero(Hero("Battle-Game-Images/Goblin-copy.jpg", "Goblin", 500))
            number_enemies -= 1
        x = 50
        for enemy in enemies.heroes:
            enemy.move(x, 50)
            x += 400


    # Update the display
    pygame.display.flip()
    clock.tick(60)
