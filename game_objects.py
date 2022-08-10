import pygame

pygame.init()
megatronSound = pygame.mixer.Sound('static/music/ANIM_DECEPTICON_LG_ROLL_01.WAV')
megatronSound.set_volume(0.1)

def _load_img(images: list) -> list:
    return [pygame.image.load(img) for img in images]


class Player:
    walkRight = _load_img([f'static/optimus_prime/prime_move/right_{i}.png' for i in range(1, 7)])
    walkLeft = _load_img([f'static/optimus_prime/prime_move/left_{i}.png' for i in range(1, 7)])
    shoot_right = _load_img([f'static/optimus_prime/shoots/Shoot_{i}.png' for i in range(1, 3)])
    shoot_left = _load_img([f'static/optimus_prime/shoots/Shoot_{i}_left.png' for i in range(1, 3)])
    transformLeft = [pygame.image.load('static/optimus_prime/prime_transform/Transform1_left.png'),
                     pygame.image.load('static/optimus_prime/prime_transform/Transform2_left.png'), pygame.image.load(
            'static/optimus_prime/prime_transform/Transform3_left.png'),
                     pygame.image.load('static/optimus_prime/prime_transform/Transform4_left.png'), pygame.image.load(
            'static/optimus_prime/prime_transform/Transform5_left.png')]
    transformRight = [pygame.image.load('static/optimus_prime/prime_transform/Transform1.png'),
                      pygame.image.load('static/optimus_prime/prime_transform/Transform2.png'), pygame.image.load(
            'static/optimus_prime/prime_transform/Transform3.png'),
                      pygame.image.load('static/optimus_prime/prime_transform/Transform4.png'), pygame.image.load(
            'static/optimus_prime/prime_transform/Transform5.png')]
    player_fight = [pygame.image.load('static/optimus_prime/Prime_Fight/Prime_fight.png'), pygame.image.load(
        'static/optimus_prime/Prime_Fight/Prime_fight2.png'),
                    pygame.image.load('static/optimus_prime/Prime_Fight/Prime_fight3.png'),
                    pygame.image.load('static/optimus_prime/Prime_Fight/Prime_fight4.png'),
                    pygame.image.load('static/optimus_prime/Prime_Fight/Prime_fight5.png'),
                    pygame.image.load('static/optimus_prime/Prime_Fight/Prime_fight6.png'),
                    pygame.image.load('static/optimus_prime/Prime_Fight/Prime_fight7.png'),
                    pygame.image.load('static/optimus_prime/Prime_Fight/Prime_fight8.png'),
                    pygame.image.load('static/optimus_prime/Prime_Fight/Prime_fight9.png'),
                    pygame.image.load('static/optimus_prime/Prime_Fight/Prime_fight10.png'),
                    pygame.image.load('static/optimus_prime/Prime_Fight/Prime_fight11.png'),
                    pygame.image.load('static/optimus_prime/Prime_Fight/Prime_fight12.png'),
                    pygame.image.load('static/optimus_prime/Prime_Fight/Prime_fight13.png'),
                    pygame.image.load('static/optimus_prime/Prime_Fight/Prime_fight14.png')]
    transformRightRev = [pygame.image.load('static/optimus_prime/prime_transform/Transform5.png'),
                         pygame.image.load('static/optimus_prime/prime_transform/Transform4.png'), pygame.image.load(
            'static/optimus_prime/prime_transform/Transform3.png'),
                         pygame.image.load('static/optimus_prime/prime_transform/Transform2.png'), pygame.image.load(
            'static/optimus_prime/prime_transform/Transform1.png')]
    drive_right = [pygame.image.load('static/optimus_prime/prime_drive/drive_right_1.png'), pygame.image.load(
        'static/optimus_prime/prime_drive/drive_right_2.png'),
                   pygame.image.load('static/optimus_prime/prime_drive/drive_right_3.png'), pygame.image.load(
            'static/optimus_prime/prime_drive/drive_right_4.png')]
    drive_left = [pygame.image.load('static/optimus_prime/prime_drive/drive_right_1.png'), pygame.image.load(
        'static/optimus_prime/prime_drive/drive_right_2.png'),
                  pygame.image.load('static/optimus_prime/prime_drive/drive_right_3.png'), pygame.image.load(
            'static/optimus_prime/prime_drive/drive_right_4.png')]
    player_jump = [pygame.image.load('static/optimus_prime/Prime_jump/jump_1.png'),
                   pygame.image.load('static/optimus_prime/Prime_jump/jump_2.png'), pygame.image.load(
            'static/optimus_prime/Prime_jump/jump_3.png'),
                   pygame.image.load('static/optimus_prime/Prime_jump/jump_4.png'), pygame.image.load(
            'static/optimus_prime/Prime_jump/jump_5.png'), ]
    take_cover = pygame.image.load('static/optimus_prime/prime_sit_down/Prime_sit_down.png')
    playerStand = pygame.image.load('static/optimus_prime/prime_idle/idle.png')

    def __init__(self, x, y, y2, width, height):
        self.x = x
        self.y = y
        self.y2 = y2
        self.width = width
        self.height = height
        self.speed = 5
        self.truck_speed = 7
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.shoot_r = False
        self.shoot_l = False
        self.tfleft = False
        self.tfright = False
        self.tfrightrev = False
        self.drive_r = False
        self.drive_l = False
        self.cover = False
        self.fight = False
        self.animCount = 0
        self.fightCount = 0
        self.lastMove = 'right'
        self.transformCount = 0
        self.hitbox = (self.x, self.y, 40, 60)
        self.state = "robot"

    def draw(self, win):
        if self.animCount + 1 >= 30:
            self.animCount = 0
        if self.transformCount + 1 >= 80:
            transformCount = 40
        if self.fightCount + 1 >= 80:
            self.fightCount = 0
        if self.left:
            win.blit(self.walkLeft[self.animCount // 5], (self.x, self.y))
            self.animCount += 1
        elif self.right:
            win.blit(self.walkRight[self.animCount // 5], (self.x, self.y))
            self.animCount += 1
        elif self.shoot_r:
            win.blit(self.shoot_right[self.animCount // 18], (self.x, self.y))
            self.animCount += 1
        elif self.shoot_l:
            win.blit(self.shoot_left[self.animCount // 18], (self.x, self.y))
            self.animCount += 1
        elif self.fight:
            win.blit(self.player_fight[self.fightCount // 6], (self.x, self.y))
            self.fightCount += 2
            # win.blit(player_fight[animCount // 3], (x, y))
            # animCount += 1
        elif self.tfleft:
            win.blit(self.transformLeft[self.animCount // 6], (self.x, self.y))
            self.animCount += 1
        elif self.tfright:
            win.blit(self.transformRight[self.animCount // 6], (self.x, self.y2))
            self.animCount += 3
            if self.transformRight[self.animCount // 6] == self.transformRight[-1]:
                self.tfright = False
                self.animCount = 0
                self.drive_r = True

            # win.blit(playerVehicle, (x, y2))
            # win.blit(transformRight[transformCount // 18], (x, y2))
            # transformCount += 3
        elif self.tfrightrev:
            win.blit(self.transformRightRev[self.animCount // 6], (self.x, self.y2))
            self.animCount += 3
            if self.transformRightRev[self.animCount // 6] == self.transformRightRev[-1]:
                self.tfrightrev = False
                self.animCount = 0
            # win.blit(playerVehicle, (x, y2))
            # if not tfright:
            # return win.blit(playerStand, (x, y))
        elif self.drive_r:
            win.blit(self.drive_right[self.animCount // 12], (self.x, self.y2))
            self.animCount += 1
        elif self.isJump:
            win.blit(self.player_jump[self.animCount // 6], (self.x, self.y))  # прыжок
        elif self.cover:
            win.blit(self.take_cover, (self.x, self.y2))
            # animCount += 1
        # elif drive_l:
        # win.blit(drive_left [animCount // 12], (x, y2))
        # animCount += 1
        else:
            win.blit(self.playerStand, (self.x, self.y))
        self.hitbox = (self.x, self.y, 40, 60)
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        # pygame.draw.rect(win, self.hitbox, 2)
        # win.blit(playerStandAction [animCount // 2], (x, y))
        # animCount += 1

    def hit(self, win):
        self.isJump = False
        self.jumpCount = 10
        self.x -= 50
        self.y = 425
        self.animCount = 0
        font1 = pygame.font.SysFont('comicsans', 25)
        text = font1.render("Don't let Megatron obtain the Allspark", 1, (255, 0,0))
        win.blit(text, (250 - (text.get_width()/2), 200))
        pygame.display.update()
        i = 0
        while i < 100:
            pygame.time.delay(10)
            i += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                i = 301
                pygame.quit()


class ProjectIle:
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = 3
        self.colour = color
        self.facing = facing
        self.vel = 8 * facing  # скорость снаряда

    def draw(self, win):
        pygame.draw.circle(win, self.colour, (self.x, self.y), self.radius)  # win то коно в котором рисуем снаряды


class Enemy:
    walkRight = [pygame.image.load('static/Megatron/Megatron_right.png'), pygame.image.load(
        'static/Megatron/Megatron_right_2.png'),
                 pygame.image.load('static/Megatron/Megatron_right_3.png'), pygame.image.load(
            'static/Megatron/Megatron_right_4.png'),
                 pygame.image.load('static/Megatron/Megatron_right_5.png'), pygame.image.load(
            'static/Megatron/Megatron_right_6.png')]
    walkLeft = [pygame.image.load('static/Megatron/Megatron_left.png'), pygame.image.load(
        'static/Megatron/Megatron_left_2.png'),
                pygame.image.load('static/Megatron/Megatron_left_3.png'), pygame.image.load(
            'static/Megatron/Megatron_left_4.png'),
                pygame.image.load('static/Megatron/Megatron_left_5.png'), pygame.image.load(
            'static/Megatron/Megatron_left_6.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.animCount = 0
        self.speed = 4
        self.hitbox = (self.x, self.y, 60, 70)
        self.health = 50  # 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.animCount + 1 >= 33:
                self.animCount = 0
                megatronSound.play()

            if self.speed > 0:
                win.blit(self.walkRight[self.animCount // 6], (self.x, self.y))
                self.animCount += 1
            else:
                win.blit(self.walkLeft[self.animCount // 6], (self.x, self.y))
                self.animCount += 1

            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (1 * (50 - self.health)), 10))
            self.hitbox = (self.x, self.y, 70, 70)
            # pygame.draw.rect(win, (255, 0, 0), self.hitbox,2)
        # else:
        #     pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
        #     pygame.draw.rect(win, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (1 * (50 - self.health)), 10))
    def move(self):
        if self.speed > 0:
            if self.x + self.speed < self.path[1]:
                self.x += self.speed
            else:
                self.speed = self.speed * -1
                self.animCount = 0
        else:
            if self.x - self.speed > self.path[0]:
                self.x += self.speed
            else:
                self.speed = self.speed * -1
                self.animCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
