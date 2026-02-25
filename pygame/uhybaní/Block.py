import pygame
from settings import * 
class Block(pygame.sprite.Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load(B_IMG)
        self.image = pygame.transform.scale(self.image,(B_WIDTH,B_HEIGHT))
        self.rect = self.image.get_rect(bottom =y, centerx = x)


    


if __name__ == "__main__":
    import main
