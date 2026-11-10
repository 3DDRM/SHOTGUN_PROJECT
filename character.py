import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, image, width, height):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect.center = (x, y)

    def movement(self, delta_x, delta_y):
        self.rect.x = self.rect.x + delta_x
        self.rect.y = self.rect.y + delta_y

    def draw(self, interface):
        interface.blit(self.image, self.rect)
        #pygame.draw.rect(interface, (255, 255, 0), self.shape)