import pygame as pg
from Settings import *

class Map:
    def __init__(self, filename):
        # creating the data for building the map using a list
        self.data = []
        # open a specific file and close it with 'with'
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line.strip())

        # 
        self.tilewidth = len(self.data[0])
        self.tileheight = (len(self.data))
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE
        



#This class creates a countdown timer for a cooldown
class Cooldown:
    def __init__(self, time):
        self.start_time = 0
        # allows us to set property for cooldown time
        self.time = time
    def start(self): # counts timer in milliseconds
        self.start_time = pg.time.get_ticks()
    def ready(self): # starts timer
        # sets current time to 
        current_time = pg.time.get_ticks()
        # if the difference between current and start time are greater than self.time
        # return True
        if current_time - self.start_time >= self.time: #sees how much time has passed
            return True
        return False