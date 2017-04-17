#This is going to be a bot that runs through a random generated maze
import time
import copy
import MazeMap
import random
class MazeBot:
        def __init__(self,size=(81,21)):
            self.blocked = []
            self.maze = MazeMap.Maze(size[0],size[1])
            self.position = self.maze.getStartPos()
            self.lastposition = None
            self.goalDone = False
            self.end = None
            self.map_list = copy.deepcopy(self.maze.M)


        def map(self):
            map_list2 = copy.deepcopy(self.map_list)
            map_list2[self.position[1]][self.position[0]] = 'botObject'
            rslt = ""
            for y in range(len(map_list2)):
                for x in range(len(map_list2[0])):
                    if self.maze.isWall((x, y)):
                        rslt += '\033[42m \033[49m'
                    elif self.isApple((x, y)):
                        rslt += '\033[32mX\033[39m'
                    elif map_list2[y][x] == "botObject":
                        rslt += '\033[45m \033[49m'
                    elif self.isBlocked((x, y)):
                        rslt += '\033[41m \033[49m'
                    else:
                        rslt += ' '
                rslt += '\n'
            return "\033[f" + rslt

        def __str__( self ):
            return self.map()

        def isApple(self, pos):
            goalReached = self.maze.isGoal(pos)
            return goalReached

        def radar(self):
            self.walkable = []
            directions = [(1,0), (0,1), (-1,0), (0,-1)]
            for test_dir in directions:
                new_pos = (self.position[0] + test_dir[0], self.position[1] + test_dir[1])
                if self.isApple(new_pos):
                    self.goalDone = True
                    break
                block = self.isBlocked(new_pos)

                if block == False and self.maze.isWall(new_pos) == False:
                    self.walkable.append(new_pos)

        def isBlocked(self, pos):
            return pos in self.blocked




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
                    self.end = False

                rand = random.randrange(len(options))
                self.lastposition = self.position
                self.position = options[rand]



        def engine(self):
            #print(self.position)
            a = None
            x = 0
            y = time.time()
            while a != True:
                x += 1
                print(self,flush=True)
                time.sleep(0.02)

                #print(x)
                #if x/30 == int(x/30):
                #    a = self.blocked
                #print(a)
                a = self.walk()
                #time.sleep(0.05)
            p = time.time()
            print(self.map())
            print("The bot had to take %d steps and it took %d seconds" % (x, p - y))

bot = MazeBot((101,51))
bot.engine()

# vim: set expandtab    
