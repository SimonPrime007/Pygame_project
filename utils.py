import pygame


def drawWindow(win, bg, font, score, Prime, Megatron, bullets) -> None:
    win.blit(bg, (0, 0))
    text = font.render('Score: ' + str(score), 1, (0, 0, 0))
    win.blit(text, (350, 10))
    Prime.draw(win)
    if Megatron.visible:
        Megatron.draw(win)

    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()
