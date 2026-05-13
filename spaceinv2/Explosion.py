import pygame
import settings

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.animation = [pygame.image.load(settings.EXPLOSION_IMAGE_PATH.format(i)).convert_alpha() for i in range(1, 6)]
        self.curent_image = 0
        self.image = self.animation[self.curent_image]
        self.rect = self.image.get_rect(center=(x, y))
        self.animation_speed = 100 # milliseconds 
        self.last_update = pygame.time.get_ticks() 

    def update(self):
        self.curent_time = pygame.time.get_ticks()
        if self.curent_time - self.last_update > self.animation_speed:
            self.curent_image += 1
            if self.curent_image < len(self.animation):
                self.image = self.animation[self.curent_image]
                self.last_update_time = self.curent_time
            else:
                self.kill()