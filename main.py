import pygame, sys
from pygame.locals import *

class Player:
    x=0
    y=0
    sprite = pygame.sprite.Sprite()

    def __init__(self,x,y,system):
        self.x=x
        self.y=x
        self.sprite.image=pygame.Surface([32,32])
        self.sprite.image.fill(Color(0,255,0))
        self.sprite.rect=self.sprite.image.get_rect()
        self.sprite.rect.x=self.x
        self.sprite.rect.y=self.y

        system.spritelist.add(self.sprite)

    def update(self):
        self.sprite.rect.x=self.x
        self.sprite.rect.y=self.y

class System:
    spritelist=pygame.sprite.Group()
    
    def __init__(self):
        pass

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Hello Pygame World!')
        player = Player(400,400,self)
        clock=pygame.time.Clock()
        while True: # main game loop

            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player.y-=5
                    elif event.key == pygame.K_DOWN:
                        player.y+=5
                    if event.key == pygame.K_LEFT:
                        player.x-=5
                    elif event.key == pygame.K_RIGHT:
                        player.x+=5

            #player.update()

            self.spritelist.draw(screen)
            clock.tick(30)
            pygame.display.flip()
            screen.fill(Color(0,0,0))


system = System()
system.run()

