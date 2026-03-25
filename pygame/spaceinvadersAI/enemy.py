import pygame
import random

class Enemy:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0, 760), 0, 40, 40)
        self.speed = random.randint(2, 4)

    def update(self):
        self.rect.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)