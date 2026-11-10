import pygame

class Weapon():
    def __init__(self, image, width, height):
        self.image = image
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()

    def update(self, player):
        self.rect.center = player.rect.center
        self.rect.x = self.rect.x + player.rect.width - 40
        self.rect.y = self.rect.y + player.rect.height - 55
        
    def draw(self, interface):
        interface.blit(self.image, self.rect)