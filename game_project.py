import pygame
import constants
import objects
import enemy
import enemy2
import enemy3
import character
import weapon
import bullet

pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode((constants.DISPLAY_WIDTH, constants.DISPLAY_HEIGHT))
pygame.display.set_caption('CHIMO ADVENTURE SUPREME')
window.fill((0,0,0))

music = pygame.mixer.music.load('assets//songs//practice_mode.mp3')
music = pygame.mixer.music.play(-1)

x = 500
y = 300

player_image = pygame.image.load('assets//images//characters//player//shovel_knight.png').convert_alpha()
background = pygame.image.load('assets//images//backgrounds//Stage_1.png').convert()

player_image = pygame.transform.scale(player_image, (70, 70))
background = pygame.transform.scale(background, (constants.STAGE_WIDTH, constants.STAGE_HEIGHT))

player = character.Character(x, y, player_image,  100, 80)

#player_width = player.shape.width
#player_height = player.shape.height

walls =[
    objects.Wall(40, 440, 210, 90),
    objects.Wall(700, 120, 50, 150),
    objects.Wall(50, 135, 40, 40),
    objects.Wall(705, 450, 80, 110)
]

ammu = []
ammu2 = []

enemy_image = pygame.image.load('assets//images//characters//enemy//spider_two.png').convert_alpha()
enemy_image_two = pygame.image.load('assets//images//characters//enemy//spider.png').convert_alpha()
gun_image = pygame.image.load('assets//images//weapons//shotgun.png').convert_alpha()
shot_image = pygame.image.load('assets//images//weapons//bullet.png').convert_alpha()
shot_image_left = pygame.image.load('assets//images//weapons//bullet2.png').convert_alpha()

enemie1 = enemy.Enemy(100, 200, enemy_image, 120, 100, 100, 20)
enemie2 = enemy2.Enemy(400, 400, enemy_image, 120, 100, 100, 20)
enemie3 = enemy3.Enemy(480, 150, enemy_image_two, 120, 100, 100, 20)

enemies = [enemie1, enemie2, enemie3]

gun = weapon.Weapon(gun_image, 70, 30)

text = pygame.font.Font(None, 60)
text_image = text.render('Score:', True, (0, 0, 0))

loocking_right = True
clock = pygame.time.Clock()
game = True
switch_bullet = True
while game:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        if switch_bullet:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:
                    right_bullet = bullet.Bullet(gun, shot_image_left, -10, 40, 30)
                    ammu2.append(right_bullet)
                    switch_bullet = False

        if not switch_bullet:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_k:
                    left_bullet = bullet.Bullet(gun, shot_image, 10, 40, 30)
                    ammu.append(left_bullet)
                    switch_bullet = True

    pressed = pygame.key.get_pressed()

    delta_x = 0
    delta_y = 0

    if pressed[pygame.K_w]:
        delta_y -= constants.SPEED
        player.movement(0, delta_y)

    if pressed[pygame.K_s]:
        delta_y += constants.SPEED
        player.movement(0, delta_y)

    if pressed[pygame.K_d]:
        delta_x += constants.SPEED
        player.movement(delta_x, 0)
        if loocking_right:
            player.image = pygame.transform.flip(player.image, True, False)
            gun.image = pygame.transform.flip(gun.image, True, False)
            loocking_right = False

    if pressed[pygame.K_a]:
        delta_x -= constants.SPEED
        player.movement(delta_x, 0)
        if not loocking_right:
            player.image = pygame.transform.flip(player.image, True, False)
            gun.image = pygame.transform.flip(gun.image, True, False)
            loocking_right = True       
        
    if player.rect.x > (window.get_width() - player.rect.width - 40):
        player.rect.x = window.get_width() - player.rect.width - 40

    if player.rect.x < 35:
        player.rect.x = 35

    if player.rect.y > (window.get_height() - player.rect.height - constants.EDGE):
        player.rect.y = window.get_height() - player.rect.height - constants.EDGE

    if player.rect.y < 80:
        player.rect.y = 80

    for i in walls:
        if player.rect.colliderect(i.rect):
            player.rect.x = player.rect.x - delta_x
            player.rect.y = player.rect.y - delta_y

    gun.update(player)

    window.fill((0,0,0))
    window.blit(background, (0, 0))
    window.blit(text_image, (20, 20))     
    
    for i in enemies:
        i.update()
        i.draw(window)          

    player.draw(window)
    gun.draw(window)

    for i in ammu[:]:
        i.update()
        i.draw(window)
        if i.rect.x > (window.get_width() - i.rect.width - 35):
            ammu.remove(i)
            continue
        for fuck in enemies[:]:
            if i.rect.colliderect(fuck.rect):
                fuck.health -= 10
                if i in ammu:
                    ammu.remove(i)
                if fuck.health <= 0:
                    enemies.remove(fuck)
                break

    for p in ammu2[:]:
        p.update()
        p.draw(window)
        if p.rect.x < 60:
            ammu2.remove(p)
            continue

        for d in enemies[:]:
            if p.rect.colliderect(d.rect):
                d.health -= 10
                if p in ammu2:
                    ammu2.remove(p)
                if d.health <= 0:
                    enemies.remove(d)
                break


    #for enemie in enemies:
        #pygame.draw.rect(window, (255, 0, 0), enemie.rect)

    pygame.display.update()

pygame.quit()
