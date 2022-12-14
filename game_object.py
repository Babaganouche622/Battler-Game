import pygame

class GameObject(pygame.sprite.Sprite):
    """This is the generic game object for all ingame sprites. 
    We make all allies and enemies starting with the basic class."""
    def __init__(self, x, y, image):
        super(GameObject, self).__init__()
        self.surf = pygame.image.load(image)
        self.x = x
        self.y = y
        self.rect = self.surf.get_rect()

    def render(self, screen):
        self.rect.x = self.x
        self.rect.y = self.y
        screen.blit(self.surf, (self.x, self.y))

    def move(self, x, y):
        self.x = x
        self.y = y
