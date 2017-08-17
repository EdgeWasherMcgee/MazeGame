#This is going to be a bot that runs through a random generated maze
#\033[2D = Flytta bakåt 2 steg vänster(D), C höger, A upp, B ner
#\033[3;12F = Första Rad, andra Kolumn, ; för att skillja dem åt
import time
import copy
import MazeMap
import random
from ANSI import *
class MazeBot:
        def __init__(self, pos1=71, pos2=31):
            self.blocked = []
            self.maze = MazeMap.Maze(pos1, pos2)
            self.position = self.maze.getStartPos()
            self.lastposition = None
            self.goalDone = False
            self.end = None
            self.map_list = copy.deepcopy(self.maze.M)


        def printB(self, x, y):
            return "\033[%d;%df" % (y, x) + ANSI.redB + ' ' + ANSI.defaultB

        def printY(self):
            return "\033[%d;%df" % (self.position[1], self.position[0]) + ANSI.magentaB + ' ' + ANSI.defaultB


        def map(self):
            map_list2 = copy.deepcopy(self.map_list)
            map_list2[self.position[1]][self.position[0]] = 'botObject'
            rslt = ""
            for y in range(len(map_list2)):
                for x in range(len(map_list2[0])):
                    if self.maze.isWall(x, y):
                        rslt += '\033[42m \033[49m'
                    elif self.isApple(x, y):
                        rslt += '\033[46m \033[49m'
                    elif self.maze.getStartPos() == (x, y):
                        rslt += '\033[45m \033[49m'
                    elif map_list2[y][x] == "botObject":
                        rslt += '\033[35mY\033[39m\033[52m\033[49m'
                    elif self.isBlocked(x, y):
                        rslt += '\033[41m \033[49m'
                    else:
                        rslt += ' '
                rslt += '\n'
            return "\033[f" + rslt





        def isApple(self, pos1, pos2):
            goalReached = self.maze.isGoal(pos1, pos2)
            return goalReached

        def radar(self):
            self.walkable = []
            directions = [(1,0), (0,1), (-1,0), (0,-1)]
            for test_dir in directions:
                new_pos = (self.position[0] + test_dir[0], self.position[1] + test_dir[1])
                if self.isApple(new_pos[0], new_pos[1]):
                    self.goalDone = True
                    break
                block = self.isBlocked(new_pos[0], new_pos[1])

                if block == False and self.maze.isWall(new_pos[0], new_pos[1]) == False:
                    self.walkable.append(new_pos)

        def isBlocked(self, x, y):
            for test_block in self.blocked:
                if x == test_block[0] and y == test_block[1]:
                    return True
            return False




        def walk(self):
                self.radar()
                options = self.walkable.copy()
                if self.goalDone:
                    print("The bot has reached the goal!")
                    return True
                if len(self.walkable) > 1:
                    for y in range(len(self.walkable)):
                        if self.walkable[y] == self.lastposition:
                            options.pop(y)
                else:
                    self.end = True

                if self.end and len(self.walkable) > 2:
                    self.blocked.append(self.lastposition)
                    self.printB(self.lastposition[0], self.lastposition[1])
                    self.end = False

                rand = random.randrange(len(options))
                self.lastposition = self.position
                #print(self.printY())
                self.position = options[rand]



        def engine(self):
            #print(self.position)
            a = None
            x = 0
            y = time.time()
            print('\033c')
            print(self.map())
            while a != True:
                x += 1
                print(self.map())
                #if x%3 == 0:
                #print(x)
                #if x/30 == int(x/30):
                #    a = self.blocked
                #print(a)
                a = self.walk()
                time.sleep(0.041)
            p = time.time()
            '\033[f'
            print("The bot had to take %d steps and it took %d seconds" % (x, p - y))
            #print(self.map())
            restart = input("Do you want to start again?\n")
            if restart.lower() == 'yes' or restart.lower() == 'y':
                ps1 = input("SizeX")
                ps2 = input("SizeY")
                if ps1 == '' and ps2 == '':
                    self.__init__(71, 31)
                else:
                    self.__init__(int(int(ps1), int(ps2)))
                self.engine()
            else:
                print("Bye!")
# vim: set expandtab    
