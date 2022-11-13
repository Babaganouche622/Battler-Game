from game_object import GameObject
import pygame

class Button():
    """
    This class is the basis for all buttons in that apear during run time. 
    We take the coordinate positional arguments, the image file, and the scale ratio.
    Then we transform them into the clickable game object that returns a true/false 
    statement that allows us to create user interaction.
    """
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        """This is how we make the button visibile, we call this during run-time."""
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action
        