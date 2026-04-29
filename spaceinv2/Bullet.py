
#class Bullet(pygame.sprite.Sprite):
import pygame
import settings  
import random
class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,kdo_vystrelil="alien"):
        super().__init__()
        kdo_vystrelil = kdo_vystrelil
        if kdo_vystrelil == "alien":
            self.image = pygame.image.load(settings.ENEMY_BULLET_IMG_PATH).convert_alpha()
            self.rect =self.image.get_rect(center = (x,y))
            self.speed = settings.ENEMY_BULET_SPEED
        else:
            self.image = pygame.image.load(settings.PLAYER_BULLET_IMG_PATH).convert_alpha()
            self.rect =self.image.get_rect(center = (x,y))
            self.speed = settings.PLAYER_BULET_SPEED * -1

    def update(self):

        self.rect.y += self.speed
        if self.rect.bottom <0 or self.rect.top > settings.SCREEN_HEIGHT:
            self.kill()

    


if __name__ == "__main__":
    import main
