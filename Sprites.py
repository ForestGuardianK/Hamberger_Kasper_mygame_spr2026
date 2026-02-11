import pygame as pg
from pygame.sprite import Sprite
from Settings import *

vec = pg.math.Vector2

class Player(Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.vel = vec(0,0)
        self.pos = vec(x,y) * TILESIZE
    def get_keys(self):
        self.vel = vec(0,0)
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.vel.x = -PLAYER_SPEED
        if keys[pg.K_d]:
            self.vel.x = PLAYER_SPEED
        if keys[pg.K_w]:
            self.vel.y = -PLAYER_SPEED
        if keys[pg.K_s]:
            self.vel.y = PLAYER_SPEED
        if self.vel.x != 0 and self.vel.y != 0:
            self.vel *= 0.7071

    def update(self):
        print("player updating")
        self.get_keys()
        self.rect.center = self.pos
        self.pos += self.vel * self.game.dt

# enemy
class Mob(Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.vel = vec(0,0)
        self.pos = vec(x,y) * TILESIZE
        self.rect.center = self.pos
    # def update(self):
    #     pass
    def update(self):
        hits = pg.sprite.spritecollide(self, self.game.all_walls, True)
        if hits:
             print("collided")
             #self.pos += self.speed * self.vel 
        self.pos -= self.game.player.pos*self.game.dt
        self.rect.center = self.pos
        self.pos += self.vel * self.game.dt
        self.vel = vec(480,480)

class Goal(Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        Sprite.__init__(self, self.groups)
        self.game = game
       
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.vel = vec(0,0)
        self.pos = vec(x,y) * TILESIZE
        self.rect.topleft = self.pos
        self.score = 0
 
 
    def update(self):
        self.rect.center = self.pos
        if self.rect.colliderect(self.game.mob.rect):
            self.score += 1
            print(self.score)
            print("GOALLL")

# objects
class Wall(Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.all_walls
        Sprite.__init__(self, self.groups)
        self.game = game
       
        self.image = pg.Surface((TILESIZE, TILESIZE ))
        self.image.fill(GRAY)
        self.rect = self.image.get_rect()
        self.vel = vec(0,0)
        self.pos = vec(x,y) * TILESIZE
        self.rect.center = self.pos
    def update(self):
        pass
 
class Coin(Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.all_walls
        Sprite.__init__(self, self.groups)
        self.game = game
       
        self.image = pg.Surface((TILESIZE, TILESIZE ))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.vel = vec(0,0)
        self.pos = vec(x,y) * TILESIZE
        self.rect.topleft = self.pos
        self.score = 0
    def update(self):
        pass
