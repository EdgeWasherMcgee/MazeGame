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
#   Organization is that top left corner is point (0,0)
#               

import random

class Maze:
    wallObject = "Wall"
    spaceObject = "Space"
    goalObject = "apple"

    def __init__(self, size_x = 21, size_y = 21 ):
        if 0 == size_x % 2 or 0 == size_x % 2:
            print("Should be called with odd arguments")
            return

        self.size_x = size_x
        self.size_y = size_y

        self.createMaze()


    def createMaze(self): 

        self.tails = []
        self.M = []

        self.__fillWithWalls()
        self.start_x = 1 + 2 * random.randrange( (self.size_x - 1) / 2)
        self.start_y = 1 + 2 * random.randrange( (self.size_y - 1) / 2)

        self.MazeWalk(self.start_x, self.start_y)

        # Put an apple in one of the tails
        i = random.randrange( len( self.tails ) )
        self.M[ self.tails[i][1]][ self.tails[i][0] ] = Maze.goalObject



    def getStartPos( self ):
        return (self.start_x, self.start_y)

    def __fillWithWalls(self):
        for y in range(self.size_y):
            row = list()
            for x in range(self.size_x):
                row.append( Maze.wallObject )
            self.M.append( row )

    def isWall( self, x, y ):
        return self.M[y][x] == Maze.wallObject

    def isGoal( self, x, y ):
        return self.M[y][x] == Maze.goalObject
    
    def isDiggable( self, x, y ):
        if x <= 0: return False
        if x >=  self.size_x - 1: return False
        if y <= 0: return False
        if y >=  self.size_y - 1: return False
        return self.isWall( x, y)

    def dig( self, fr, step ):
        self.M[ fr[1] + int(step[1] / 2) ][ fr[0] + int(step[0] / 2)] = Maze.spaceObject
        self.M[ fr[1] + step[1]    ][ fr[0] + step[0]    ] = Maze.spaceObject

    def __str__( self ):
        rslt = ""
        for y in range( self.size_y ):
            for x in range( self.size_x ):
                if self.isWall(x,y):
                    rslt += "O"
                elif self.isGoal(x,y):
                    rslt += '\033[32mX\033[39m'
                else:
                    rslt += " "
            rslt += "\n"

        return rslt

    #directions = [ (1,0), (0,1), (-1,0), (0,-1) ]



    def MazeWalk( self, start_x, start_y ):

        # Check calling variables
        if 0 == start_x % 2 or 0 == start_x % 2:
            print("Should be called with odd arguments")
            return

        # Make a list that tells the way back. 
        last_pos = []

        here_x = start_x
        here_y = start_y

        self.M[ here_y ][ here_x ] = Maze.spaceObject

        # 1. see if there is a way to go
        # 2. if so take the step and save last place
        # 3. otherwise take a step back if there is, otherwise doen

        forward = True
    
        while True:
            #print( self )
            avail_dirs = [ (2,0), (0,2), (-2,0), (0,-2) ]
            dirs = []
            for d in avail_dirs:
                if self.isDiggable( here_x + d[0], here_y + d[1] ):
                    dirs.append( d )

            if 0 == len( dirs ):
                # check if we are at the starting position. then leave
                if forward:
                    self.tails.append( (here_x, here_y) )

                if len( last_pos ) == 0: return 
                # take a step back
                (here_x,here_y) = last_pos.pop()
                forward = False
            else:
                # Add current position to last_pos
                last_pos.append( (here_x, here_y) )
                # select one of the directions
                step = dirs[ random.randint(0, len(dirs) - 1) ]
                # take that step and dig it
                self.dig( (here_x,here_y), step)
                here_x += step[0]
                here_y += step[1]
                forward = True
                # start over

