import pygame

from game_objects import Player, ProjectIle, Enemy
from utils import drawWindow

if __name__ == '__main__':

    pygame.init()
    win = pygame.display.set_mode((500, 500))

    pygame.display.set_caption("Игра_в_питоне")
    pygame.display.set_icon(pygame.image.load("icon.png"))

    player_block = pygame.image.load('static/optimus_prime/Prime_Fight/Prime_block.png')

    bg = pygame.image.load('bg.jpg')

    # playerStandAction = [pygame.image.load('idle2.png'), pygame.image.load('idle3.png'), pygame.image.load('idle4.png')]

    playerVehicle = pygame.image.load('drive_right_1.png')

    clock = pygame.time.Clock()

    # bulletSound = pygame.mixer.Sound('')
    # bulletSound.play()
    # hitSound = pygame.mixer.Sound('hit.wav')
    # walkSound = pygame.mixer.Sound('walk.wav')

    music = pygame.mixer.music.load('static/music/MX_HOOVER_EXT_BOSS_DEC_1.mp3')
    pygame.mixer.music.play(-1)

    score = 0

    # x = 50
    # y = 425
    # width = 37
    # height = 58

    # mainloop
    font = pygame.font.SysFont('comicsans', 20, True)
    Prime = Player(50, 425, 455, 37, 58)
    Megatron = Enemy(100, 415, 50, 70, 450)
    shootLoop = 0
    run = True
    bullets = []
    while run:
        clock.tick(30)
        # pygame.time.delay(50) #0,1 секунду это при 100

        if Megatron.visible == True:
            if Prime.hitbox[1] < Megatron.hitbox[1] + Megatron.hitbox[3] and Prime.hitbox[1] + Prime.hitbox[3] > \
                    Megatron.hitbox[1]:
                if Prime.hitbox[0] + Prime.hitbox[2] > Megatron.hitbox[0] and Prime.hitbox[0] < Megatron.hitbox[0] + \
                        Megatron.hitbox[2]:
                    # hitSound.play()
                    Prime.hit()
                    # score -= 5

        if shootLoop > 0:
            shootLoop += 3
        if shootLoop > 3:
            shootLoop = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for bullet in bullets:
            if bullet.y - bullet.radius < Megatron.hitbox[1] + Megatron.hitbox[3] and bullet.y + bullet.radius > \
                    Megatron.hitbox[1]:
                if bullet.x + bullet.radius > Megatron.hitbox[0] and bullet.x - bullet.radius < Megatron.hitbox[0] + \
                        Megatron.hitbox[2]:
                    # hitSound.play()
                    Megatron.hit()
                    score += 5
                    bullets.pop(bullets.index(bullet))

            if bullet.x < 500 and bullet.x > 0:  # bullet больше чем ноль и не вышел за границы, значит этот снаряд двигаем пока не вышел за пределы
                bullet.x += bullet.vel  # bullet и vel
            else:
                bullets.pop(bullets.index(bullet))  # элемент будет соотв элемент который перебираем по индексу

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and Prime.x > 5:
            Prime.x -= Prime.speed
            Prime.left = True
            Prime.right = False
            Prime.tfright = False
            Prime.tfleft = False
            Prime.drive_l = False
            Prime.drive_r = False
            Prime.shoot_r = False
            Prime.shoot_l = False
            Prime.lastMove = 'left'
            Prime.cover = False
            Prime.fight = False
        elif keys[pygame.K_RIGHT] and Prime.x < 500 - Prime.width - 5:
            Prime.x += Prime.speed
            Prime.left = False
            Prime.right = True
            Prime.tfright = False
            Prime.tfleft = False
            Prime.drive_l = False
            Prime.drive_r = False
            Prime.shoot_r = False
            Prime.shoot_l = False
            Prime.lastMove = 'right'
            Prime.cover = False
            Prime.fight = False
        elif keys[pygame.K_e] and Prime.x < 510 - Prime.width - 5 and shootLoop == 0:
            # bulletSound.play()
            if Prime.lastMove == 'right':
                facing = 1
            else:  # стрельба наоборот
                facing = 1  # -1

            if len(bullets) < 5:  # меньше 5 снарядов виидим # максимум 5
                bullets.append(
                    ProjectIle(round(Prime.x + Prime.width), round(Prime.y + Prime.height // 5), 5, (255, 0, 0),
                               facing))
            shootLoop = 3
            Prime.shoot_r = True
            Prime.shoot_l = False
            Prime.drive_l = False
            Prime.drive_r = False
            Prime.tfright = False
            Prime.tfleft = False
            Prime.left = False
            Prime.right = False
            Prime.cover = False
            Prime.fight = False
        elif keys[pygame.K_q] and Prime.x > 4 and shootLoop == 0:
            if Prime.lastMove == 'left':
                facing = -1
            else:
                facing = -1
            if len(bullets) < 5:  # меньше 5 снарядов виидим # максимум 5
                bullets.append(
                    ProjectIle(round(Prime.x + Prime.width // 30), round(Prime.y + Prime.height // 5), 5, (255, 0, 0),
                               facing))
            shootLoop = 3
            Prime.shoot_l = True
            Prime.shoot_r = False
            Prime.drive_l = False
            Prime.drive_r = False
            Prime.tfright = False
            Prime.tfleft = False
            Prime.left = False
            Prime.right = False
            Prime.cover = False
            Prime.fight = False
        elif keys[pygame.K_r]:
            Prime.fight = True
            Prime.cover = False
            Prime.drive_l = False
            Prime.drive_r = False
            Prime.tfrightrev = False
            Prime.tfright = False
            Prime.tfleft = False
            Prime.left = False
            Prime.right = False
            Prime.shoot_r = False
            Prime.shoot_l = False
        elif keys[pygame.K_f] and Prime.x < 500 - Prime.width - 5 and Prime.state != "car":
            Prime.drive_l = False
            Prime.drive_r = False  # если значение True выглядит куда более круто, возможно, стояло на false
            Prime.tfright = True
            Prime.tfleft = False
            Prime.left = False
            Prime.right = False
            Prime.shoot_r = False
            Prime.shoot_l = False
            Prime.cover = False
            Prime.fight = False
            Prime.state = "car"
        elif keys[pygame.K_g] and Prime.x < 500 - Prime.width - 5 and Prime.state != "robot":
            Prime.drive_l = False
            Prime.drive_r = False
            Prime.tfrightrev = True
            Prime.tfright = False
            Prime.tfleft = False
            Prime.left = False
            Prime.right = False
            Prime.shoot_r = False
            Prime.shoot_l = False
            Prime.cover = False
            Prime.fight = False
            Prime.state = "robot"
        elif keys[pygame.K_d] and Prime.x and Prime.x < 474 - Prime.width - 5:
            Prime.x += Prime.truck_speed
            Prime.tfrightrev = False
            Prime.drive_l = True
            Prime.drive_r = True
            Prime.tfright = False
            Prime.tfleft = False
            Prime.left = False
            Prime.right = False
            Prime.shoot_r = False
            Prime.shoot_l = False
            Prime.cover = False
            Prime.fight = False
        elif keys[pygame.K_a] and Prime.x > 5:
            Prime.x -= Prime.truck_speed
            Prime.drive_l = True
            Prime.drive_r = True
            Prime.tfrightrev = False
            Prime.tfright = False
            Prime.tfleft = False
            Prime.left = False
            Prime.right = False
            Prime.shoot_r = False
            Prime.shoot_l = False
            Prime.cover = False
            Prime.fight = False
        elif keys[pygame.K_DOWN]:
            Prime.cover = True
            Prime.drive_l = False
            Prime.drive_r = False
            Prime.tfrightrev = False
            Prime.tfright = False
            Prime.tfleft = False
            Prime.left = False
            Prime.right = False
            Prime.shoot_r = False
            Prime.shoot_l = False
            Prime.fight = False
        else:
            Prime.left = False
            Prime.right = False
            # Prime.tfright = False
            Prime.tfleft = False
            # Prime.tfrightrev = False
            Prime.shoot_r = False
            Prime.shoot_l = False
            Prime.cover = False
            Prime.fight = False
            # Prime.animCount = 0
        if not (Prime.isJump):
            if keys[pygame.K_SPACE]:
                Prime.isJump = True
        else:
            if Prime.jumpCount >= -10:
                if Prime.jumpCount < 0:
                    Prime.y += (Prime.jumpCount ** 2) / 2
                else:
                    Prime.y -= (Prime.jumpCount ** 2) / 2
                Prime.jumpCount -= 1  # был 1
            else:
                Prime.isJump = False
                Prime.jumpCount = 10

        drawWindow(win, bg, font, score, Prime, Megatron, bullets)

    pygame.quit()
