import pygame 

class Bullet(pygame.sprite.Sprite):
    def __init__(self, weapon, image, speed, width, height):
        super().__init__()
        self.image = image
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.center = weapon.rect.center
        self.speed = speed

    def update(self):
        self.rect.x += self.speed

    def draw(self, interface):
        interface.blit(self.image, self.rect)
