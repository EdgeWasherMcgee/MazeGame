#This is going to be a bot that runs through a random generated maze

import MazeMap as Maze
import random
class MazeBot:
        def __init__(self):
                self.position = Maze.GetStartPos()
                self.lastposition = ""

        def map(self):
                b = []
                size_x = 19
                size_y = 19
                for y in range(size_x):
                        a = []
                        for x in range(size_y):
                                a.append(isWall(x,y))
                        b.append(a[1:19] + '\n')
                print(b)

        def radar(self):
                self.left = Maze.isWall(self.position[0] - 1, self.position[1] )
                self.right = Maze.isWall(self.position[0] + 1, self.position[1] )
                self.up = Maze.isWall(self.position[0], self.position[1] - 1 )
                self.down = Maze.isWall(self.position[0], self.position[1] + 1 )


        def check(self):
                a = []
                if self.left == False:
                        a.append(str((self.position[0] + 1)) + str(self.position[1]) )
                elif self.right == False:
                        a.append(str((self.position[0] + 1)) + str(self.position[1]))
                elif self.up == False:
                        a.append(str(self.position[0]) + str((self.position[1] - 1)))
                elif self.down == False:
                        a.append(str(self.position[0]) + str((self.position[1] + 1)) )
                return a



        def walk(self):
                self.radar()
                positions = self.check()
                if len(positions) > 1:
                        for y in range(len(positions)):
                                if positions[y] == self.lastposition:
                                        positions.pop(y)
                rand = random.randrange(len(positions))
                self.lastposition = self.position
                self.position = positions[rand]


        def run(self):
                while self.position != o:
                        self.walk()
                

# vim: set expandtab	
