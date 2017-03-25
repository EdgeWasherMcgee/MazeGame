#This module holds a class that generates a random map of a maze.
# Interface:
#   create maze object by calling maze()
#       Arguments can optionally be size-x and size-y
#       Default is 20x20
#
#       Public methods:
#           toString()
#               creates a string that gives a picture of the map.
#               Walls are represented by X. 
#           isWall( x, y ) 
#               returns true if the positioin x,y is a wall.
#               

class Maze:
    
    def __init__(self, x_size = 20, y_size = 20 ):
        self.x_size
        self.y_size

        self.M = []
        self.createMaze()

    def createMaze(self):
        __makeWallsOnly(self)

    def __makeWallsOnly()
        for x in range(self.size_x):
            row = []
            for y in range(self.size_y):
                row.append("X")
            row.append( row )

