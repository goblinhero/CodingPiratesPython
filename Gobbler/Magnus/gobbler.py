import pygame, random

def init():
    global grafik, antal_fjender, point_for_fjende
    antal_fjender = 20
    point_for_fjende = 30
    grafik = [pygame.image.load('download.jpg'),
              pygame.image.load('enemy.png'),
              pygame.image.load('block.png'),
              pygame.image.load('bombe.jpg'),
              pygame.image.load('eksplosion.jpg')]
    
class Spil(object):
    def main(self,screen):
        clock = pygame.time.Clock()
        self.sprites = pygame.sprite.Group()
        self.player = Spiller(self.sprites)
        self.mines = pygame.sprite.Group()
        self.mine = Mine(self.sprites)
        self.mines.add(self.mine)
        self.walls = pygame.sprite.Group()
        self.playerWon = False
        self.playerLost = False
        for x in range(0, 640, 32):
            for y in range(0, 480, 32):
                if x in (0,640-32) or y in (0, 480-32):
                    wall = pygame.sprite.Sprite(self.walls)
                    wall.image = grafik[2]
                    wall.rect = pygame.rect.Rect((x,y), wall.image.get_size())
        self.sprites.add(self.walls)
        self.enemies = pygame.sprite.Group()
        for x in range(0,antal_fjender):
            self.addEnemy()
        while 1:
            if self.playerWon:
                return
            if self.playerLost:
                screen.blit(grafik[4], (0,0))
                pygame.display.flip()
                return
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
            dt = clock.tick(30)/1000
            self.sprites.update(dt, self)
            screen.fill((255,255,255))
            self.sprites.draw(screen)
            pygame.display.flip()
    def addEnemy(self):
        enemy = Enemy(self.enemies)
        self.enemies.add(enemy)
        self.sprites.add(enemy)

class Mine(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super(Mine, self).__init__(*groups)
        self.image = grafik[3]
        self.rect = pygame.rect.Rect((50,50),self.image.get_size())
        self.lodret = 1 #1 = Højre, -1 = Venstre
        self.vandret = 1 #1 = Ned, -1 = Op
    def update(self, dt, game):
        self.rect.x += 5*self.vandret
        self.rect.y += 5*self.lodret
        for cell in pygame.sprite.spritecollide(self, game.walls, False):
            if(cell.rect.y == 448):
                self.lodret = -1
            print(cell.rect.x)
            print(cell.rect.y)
        

class Spiller(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super(Spiller, self).__init__(*groups)
        self.image = grafik[0]
        self.rect = pygame.rect.Rect((320,240),self.image.get_size())
        self.dy = 0
        self.score = 0

    def update(self, dt, game):
        last = self.rect.copy()
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= 300 * dt
        if key[pygame.K_RIGHT]:
            self.rect.x += 300 * dt
        if key[pygame.K_SPACE]:
            self.dy = -500
        self.dy = min(400, self.dy+40)
        self.rect.y += self.dy * dt
        new = self.rect
        for cell in pygame.sprite.spritecollide(self, game.mines, False):
            print("Du tabte!")
            game.playerLost = True
        for cell in pygame.sprite.spritecollide(self, game.walls, False):
            cell = cell.rect
            if last.right <= cell.left and new.right > cell.left:
                new.right = cell.left
            if last.left >= cell.right and new.left < cell.right:
                new.left = cell.right
            if last.bottom <= cell.top and new.bottom > cell.top:
                new.bottom = cell.top
            if last.top >= cell.bottom and new.top < cell.bottom:
                new.top = cell.bottom
        for cell in pygame.sprite.spritecollide(self, game.enemies, True):
            self.score += point_for_fjende
            print("Point:",self.score)
        if len(game.enemies) == 0:
            print("Du vandt!")
            game.playerWon = True

class Enemy(pygame.sprite.Sprite):
    def __init__(self,*groups):
        super(Enemy, self).__init__(*groups)
        self.changeSpeed()
        self.image = grafik[1]
        self.rect = pygame.rect.Rect((450,240), self.image.get_size())
        self.moving = 1 #1 = Højre, -1 = Venstre
    def changeSpeed(self):
        self.speed = random.randint(1,4)
    def update(self, dt, game):
        self.rect.x += self.moving*self.speed
        for cell in pygame.sprite.spritecollide(self, game.walls, False):
            self.moving *= -1 #Skift retning
            self.changeSpeed()

if __name__ == '__main__':
    init()
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    Spil().main(screen)
