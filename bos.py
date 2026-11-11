import pygame
import bullet 

class Bos(pygame.sprite.Sprite):
    def __init__(self, x, y, bullet_list, width, height, health, speed):
        super().__init__()
        self.image = pygame.image.load('assets//images//characters//boss//corpoelec.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.shot = pygame.image.load('assets//images//weapons//transformado.png').convert_alpha()
        self.health = health
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.x = x
        self.rect.y = y
        self.bullet_list = bullet_list
        self.step = 1
        self.timer = 0
        self.tick = 60
        self.shot_timer = 0
        self.shot_tick = 40

    def update(self):
        self.timer += 1
        self.shot_timer += 1

        if self.step == 1:
            if self.timer >= self.tick:
                self.rect.y -= self.speed 
                self.timer = 0
                self.step = 2

        if self.step == 2:
            if self.timer >= self.tick:
                self.rect.y += self.speed 
                self.timer = 0
                self.step = 3
                
        if self.step == 3:
            if self.timer >= self.tick:
                self.rect.y += self.speed 
                self.timer = 0
                self.step = 4

        if self.step == 4:
            if self.timer >= self.tick:
                self.rect.y -= self.speed
                self.timer = 0
                self.step = 1

        if self.shot_timer >= self.shot_tick:
                self.shot_timer = 0
                boss_bullet = bullet.Bullet(self, self.shot, -20, 100, 100)
                self.bullet_list.append(boss_bullet)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
