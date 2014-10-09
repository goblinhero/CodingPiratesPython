import pygame, random, spil
global grafik, antal_fjender, point_for_fjende

def init():
    antal_fjender = 12
    point_for_fjende = 30
    grafik = [pygame.image.load('player.png'),
              pygame.image.load('enemy.png'),
              pygame.image.load('block.png')]

if __name__ == '__main__':
    init()
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    spil.Spil().main(screen)
