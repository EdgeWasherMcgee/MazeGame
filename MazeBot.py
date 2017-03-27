#This is going to be a bot that runs through a random generated maze

import MazeMap as Maze
import random
class MazeBot:
        def __init__(self, position):
                self.position
                self.lastposition = ''

        def radar(self):
                self.left = Maze.isWall(self.position[0] - 1, self.position[1] )
                self.right = Maze.isWall(self.position[0] + 1, self.position[1] )
                self.up = Maze.isWall(self.position[0], self.position[1] - 1 )
                self.down = Maze.isWall(self.position[0], self.position[1] + 1 )


        def check(self):
                a = []
                if self.left != 'X':
                        a.append(str((self.position[0] + 1)) + str(self.position[1]) )
                elif self.right != 'X':
                        a.append(str((self.position[0] + 1)) + str(self.position[1]))
                elif self.up != 'X':
                        a.append(str(self.position[0]) + str((self.position[1] - 1)))
                elif self.down != 'X':
                        a.append(str(self.position[0]) + str((self.position[1] + 1)) )
                return a
        


        def walk(self):
                self.radar()
                positions = self.check()
                rand = random.randrange(len(positions))
                self.lastposition = self.position
                self.position = positions[rand]
			
	





#vim: set expandtab	
