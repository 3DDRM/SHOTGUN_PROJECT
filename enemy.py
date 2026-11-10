import pygame 

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, image, width, height, speed, health):
        super().__init__()
        self.image = image
        self.image = pygame.transform.scale(self.image, (width, height))
        self.width = width
        self.height = height
        self.speed = speed
        self.health = health
        self.step = 1
        self.timer = 0
        self.tick = 60

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.timer += 1

        if self.step == 1:
            if self.timer >= self.tick:
                self.rect.x += self.speed
                self.timer = 0
                self.step = 2

        if self.step == 2:
            if self.timer >= self.tick:
                self.rect.y += self.speed
                self.timer = 0
                self.step = 3
                
        if self.step == 3:
            if self.timer >= self.tick:
                self.rect.x -= self.speed
                self.timer = 0
                self.step = 4
                
        if self.step == 4:
            if self.timer >= self.tick:
                self.rect.y -= self.speed
                self.timer = 0
                self.step = 1

    def take_damage(self, amount):
        self.health -= amount
        if self.heatlth <= 0:
            self.kill()

    def draw(self, surface):
        surface.blit(self.image, self.rect)