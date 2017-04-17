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

        self.size = (size_x,size_y)

        self.createMaze()


    def createMaze(self): 

        self.tails = []
        self.M = []
        self.start = (None,None)

        self.__fillWithWalls()
        self.start = (
                1 + 2 * random.randrange( (self.size[0] - 1) / 2),
                1 + 2 * random.randrange( (self.size[1] - 1) / 2)
                )

        self.MazeWalk(self.start)

        # Put an apple in one of the tails
        i = random.randrange( len( self.tails ) )
        self.M[ self.tails[i][1]][ self.tails[i][0] ] = Maze.goalObject



    def getStartPos( self ):
        return self.start

    def __fillWithWalls(self):
        for y in range(self.size[1]):
            row = list()
            for x in range(self.size[0]):
                row.append( Maze.wallObject )
            self.M.append( row )

    def isWall( self, pos ):
        return self.M[pos[1]][pos[0]] == Maze.wallObject

    def isGoal( self, pos ):
        return self.M[pos[1]][pos[0]] == Maze.goalObject
    
    def isDiggable( self, pos ):
        if pos[0] <= 0: return False
        if pos[0] >=  self.size[0] - 1: return False
        if pos[1] <= 0: return False
        if pos[1] >=  self.size[1] - 1: return False
        return self.isWall( pos )

    def dig( self, fr, step ):
        self.M[ fr[1] + int(step[1] / 2) ][ fr[0] + int(step[0] / 2)] = Maze.spaceObject
        self.M[ fr[1] + step[1]    ][ fr[0] + step[0]    ] = Maze.spaceObject

    def __str__( self ):
        rslt = ""
        for y in range( self.size[1] ):
            for x in range( self.size[0] ):
                pos = (x,y)
                if self.isWall(pos):
                    rslt += "O"
                else:
                    if self.isGoal(pos):
                        rslt += '\033[32mX\033[39m'
                    else:
                        rslt += " "
            rslt += "\n"

        return rslt
    
    up = (0,-2)
    down = (0,2)
    left = (-2, 0)
    right = (2,0)

    def MazeWalk( self, start ):

        # Check calling variables
        if 0 == start[0] % 2 or 0 == start[1] % 2:
            print("Should be called with odd arguments")
            return

        # Make a list that tells the way back. 
        last_pos = []

        here = start

        self.M[ here[1] ][ here[0] ] = Maze.spaceObject

        # 1. see if there is a way to go
        # 2. if so take the step and save last place
        # 3. otherwise take a step back if there is, otherwise doen

        forward = True
    
        while True:
            #print( self )
            avail_dirs = [ self.left,self.right,self.up,self.down]  
            dirs = []
            for d in avail_dirs:
                if self.isDiggable( (here[0] + d[0], here[1] + d[1])):
                    dirs.append( d )

            if 0 == len( dirs ):
                # check if we are at the starting position. then leave
                if forward:
                    self.tails.append( here )

                if len( last_pos ) == 0: return 
                # take a step back
                here = last_pos.pop()
                forward = False
            else:
                # Add current position to last_pos
                last_pos.append( here )
                # select one of the directions
                step = dirs[ random.randint(0, len(dirs) - 1) ]
                # take that step and dig it
                self.dig( here, step)
                here = ( here[0] + step[0], here[1] + step[1] )
                forward = True
                # start over

