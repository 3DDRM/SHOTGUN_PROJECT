import pygame
import constants
import objects
import enemy
import character
import weapon
import bullet
import bos

pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode((constants.DISPLAY_WIDTH, constants.DISPLAY_HEIGHT))
pygame.display.set_caption('CHIMO ADVENTURE SUPREME')
window.fill((0,0,0))

music = pygame.mixer.music.load('assets//songs//practice_mode.mp3')
music = pygame.mixer.music.play(-1)

x = 700
y = 330

player_image = pygame.image.load('assets//images//characters//player//shovel_knight.png').convert_alpha()
background = pygame.image.load('assets//images//backgrounds//stage_1.png').convert()
bc_variant = pygame.image.load('assets//images//backgrounds//sin_luz.jpg').convert()

player_image = pygame.transform.scale(player_image, (70, 70))
background = pygame.transform.scale(background, (constants.STAGE_WIDTH, constants.STAGE_HEIGHT))
bc_variant = pygame.transform.scale(bc_variant, (constants.STAGE_WIDTH, constants.STAGE_HEIGHT))

player = character.Character(x, y, player_image,  100, 80, 100)

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
ammu_boss = []

enemy_image = pygame.image.load('assets//images//characters//enemy//spider_two.png').convert_alpha()
enemy_image_two = pygame.image.load('assets//images//characters//enemy//spider.png').convert_alpha()
gun_image = pygame.image.load('assets//images//weapons//shotgun.png').convert_alpha()
shot_image = pygame.image.load('assets//images//weapons//bullet.png').convert_alpha()
shot_image_left = pygame.image.load('assets//images//weapons//bullet2.png').convert_alpha()
boss = pygame.image.load('assets//images//weapons//torchic.webp').convert_alpha()

enemie1 = enemy.Enemy(100, 200, enemy_image, 120, 100, 100, 50)
enemie2 = enemy.Enemy2(400, 400, enemy_image, 120, 100, 100, 50)
enemie3 = enemy.Enemy3(480, 150, enemy_image_two, 120, 100, 100, 50)
mayor_enemy = bos.Bos(500, 200, ammu_boss, 200, 200, 500, 80)

enemies = [enemie1, enemie2, enemie3]

gun = weapon.Weapon(gun_image, 70, 30)
text = pygame.font.Font(None, 60)
text_image = text.render(f'Score:', True, (10, 25, 47))

small_font = pygame.font.Font(None, 30)

rules_text_1 = small_font.render("WASD: Moverse", True, (0, 0, 0))
rules_text_2 = small_font.render("J / K: Disparar (3 por turno)", True, (0, 0, 0))
rules_text_3 = small_font.render("Objetivo: Derrotar enemigos", True, (0, 0, 0))

rules_text_4 = small_font.render("WASD: Moverse", True, (255, 255, 255))
rules_text_5 = small_font.render("J / K: Disparar (3 por turno)", True, (255, 255, 255))
rules_text_6 = small_font.render("Objetivo: Derrotar enemigos", True, (255, 255, 255))
rules_text_7 = small_font.render('¡¡¡¡Derrotalo y recupera la luz!!!!', True, (255, 0, 0))

player_life = pygame.font.Font(None, 60).render('Vida:', True, (0, 255, 0))

loser = False
loser_text = pygame.font.Font(None, 90).render('PERDISTE', True, (255, 0, 0))

victory = False
victory_text = pygame.font.Font(None, 70).render('¡ACABASTE CON CORPOELEC!', True, (255, 255, 0))
but = small_font.render('(pero eso no hizo que regresase la luz...)', True, (255, 255, 0))

change_stage = False

score = 0
timing = 0
boss_music = False

loocking_right = True
clock = pygame.time.Clock()
game = True
switch_bullet = True
while game:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if player.health > 0:
            if switch_bullet:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_j:
                        right_bullet = bullet.Bullet(gun, shot_image_left, -10, 40, 30)
                        ammu2.append(right_bullet)
                        timing += 1
                        if timing == 3:
                            switch_bullet = False
                            timing = 0

            if not switch_bullet:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_k:
                        left_bullet = bullet.Bullet(gun, shot_image, 10, 40, 30)
                        ammu.append(left_bullet)
                        timing += 1
                        if timing == 3:
                            switch_bullet = True
                            timing = 0

    pressed = pygame.key.get_pressed()

    delta_x = 0
    delta_y = 0

    if player.health > 0:
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
            break

    gun.update(player)

    window.fill((0,0,0))
    window.blit(background, (0, 0))
    window.blit(text_image, (20, 20))
    window.blit(player_life, (20, 60))
    window.blit(rules_text_1, (50, 480))
    window.blit(rules_text_2, (10, 510))
    window.blit(rules_text_3, (10, 540))

    if change_stage == True:
        window.blit(bc_variant, (0,0)) 
        window.blit(text_image, (20, 20))
        window.blit(player_life, (20, 60))
        window.blit(player_life, (20, 60))
        window.blit(rules_text_4, (50, 480))
        window.blit(rules_text_5, (10, 510))
        window.blit(rules_text_6, (10, 540))
        window.blit(rules_text_7, (400, 500))
    
    for i in enemies:
        i.update()
        i.draw(window)
        if player.rect.colliderect(i.rect):
            player.rect.x = 650
            player.rect.y = 290
            if player.health > 0:
                player.health -= 5
            if score > 0:
                score -= 20

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
                score += 50
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
                score += 50
                if p in ammu2:
                    ammu2.remove(p)
                if d.health <= 0:
                    enemies.remove(d)
                break

    if not enemies and mayor_enemy.health > 0:
        change_stage = True
        if not boss_music:
            pygame.mixer.music.load('assets//songs//corpoelectheme.mp3')
            pygame.mixer.music.play(-1)
            boss_music = True
        mayor_enemy.update()
        mayor_enemy.draw(window)
        if player.rect.colliderect(mayor_enemy.rect):
                player.rect.x = 100
                player.rect.y = 300
                if player.health > 0:
                    player.health -= 30
                if score > 0:
                    score -= 100

        for shots in (ammu, ammu2):
            for s in shots[:]:
                if s.rect.colliderect(mayor_enemy.rect):
                    shots.remove(s)
                    mayor_enemy.health -= 10
                    score += 50
                for colision in ammu_boss[:]:
                    if s.rect.colliderect(colision.rect):
                        ammu_boss.remove(colision)
                        break

        if mayor_enemy.health <= 0:
            victory = True
            ammu_boss.clear()

    
    for b in ammu_boss[:]:
        b.update()
        b.draw(window)
        if b.rect.x < 60:
            ammu_boss.remove(b)
            continue
        if b.rect.colliderect(player.rect):
            ammu_boss.remove(b)
            player.rect.x = 100
            player.rect.y = 300
            if score > 0:
                score -= 20
            if player.health > 0:
                player.health -= 10

    if player.health <= 0:
        loser = True

    if loser:
        window.blit(loser_text, (250, 250))

    if victory:
        window.blit(victory_text, (25, 250))
        window.blit(but, (220, 300))
            
    text_image = text.render(f'Score: {score}', True, (0, 0, 150))
    player_life = text.render(f'Vida: {player.health}', True, (0, 255, 0))

    #for enemie in enemies:
        #pygame.draw.rect(window, (255, 0, 0), enemie.rect)

    pygame.display.update()

pygame.quit()