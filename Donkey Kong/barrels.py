
import constants

class Barrels:
    '''This class defines the behavior of a general barrel.It defines barrels
    movement and their interaction with Mario (they make Mario lose lives or
    give him points).At gamelogic this class will be used as objects that are
    created and deleted when they go out of the screen. '''
    
    def __init__ (self, x: int, y: int):
        '''This method initializes the Barrels object'''
        #atributes shown in game
        self.x = x
        self.y = y
        self.isGoingDown = False #True when going down a ladder        
        #atributes not needed out of this object
        self.__haveNotCheck = True
        self.__direction = "right"
        self.__changeDirection = False
        self.__notChecked = True
        self.__notDone = True
        self.__notRevised = True
     
    #for accessing outside the private atributes
    @property
    def x (self):
        return self.__x
    @x.setter
    def x (self, x):
        self.__x = x
        
    @property
    def y (self):
        return self.__y
    @y.setter
    def y (self, y):
        self.__y = y
        
    @property
    def isGoingDown (self):
        return self.__isGoingDown
    @isGoingDown.setter
    def isGoingDown (self, isGoingDown):
        self.__isGoingDown = isGoingDown    
        
        
    
    def fall (self, board: list):
        '''This method checks if the barrel can fall and make it fall by adding values
        to the y position of it '''
        if not self.touching_floor(board) and not self.touching_ladder(board):
            self.y += 1
   
         
    def going_down (self, board: list):
        '''This method is used to see if the barrells are going down
        in a certain moment, it is exetuted constantly '''
        if self.can_go_down (board): #Goes to fuction to see if can go down
            self.isGoingDown = True
        if self.isGoingDown: #Starts going down
            if self.__notChecked:
                self.__changeDirection = True
                self.__notChecked = False
            self.y += 1
            if board [self.y + 12][self.x] == 1:
                self.isGoingDown = False
                self.__notChecked = True
                
                             
    def move (self, board: list):
        '''This method controls all the horizontal movement of the barrels,let is
        move to the left and to the right and change the direction if the barrel
        is going out of the screen. This method is also checked every frame so it
        also calls the ones that have to run every frame too.'''
        self.going_down(board)
        self.fall(board)
        if self.__direction == "right" and not self.isGoingDown:
            self.x += 2
        elif self.__direction == "left" and not self.isGoingDown:
            self.x -= 2
        #Changing direction
        if self.x not in range (0, constants.WIDTH-13) or self.__changeDirection:
            if self.__changeDirection:
                self.__changeDirection = False   
            if self.__direction == "right":
                self.__direction = "left"
            else:
                self.__direction = "right"


    def touching_ladder(self, board: list):
        '''Returns a boolean that says if the barrel is in contact with a ladder.
        It detects both up and down ladders'''
        if board [self.y + 18][self.x+5] == 2 or board[self.y + 18][self.x+5] == 3:
            return True
        else:
            return False
        
        
    def touching_floor (self, board: list):
        '''Returns a boolean that says if the barrel is in contact with the floor'''
        if board [self.y + 10][self.x + 5] == 1:
            return True
        else:
            return False
        
        
    def can_go_down (self, board: list):
        '''Returns a boolean that tells if the barrel can go down a ladder.
        Here we check the 25% of going down so 1 time out of 4 (in theory)
        it will return a true '''
        import random
        if self.touching_ladder(board):
            if self.__haveNotCheck:
                self.__haveNotCheck = False
                a = (random.randrange(0, 4) == 3)
                return a
            else:
                return False
        else:
            self.__haveNotCheck = True
            return False
        
        
    def touching_mario (self, xMario: int, yMario: int):
        '''Returns a boolean that says if the barrel is in contact with Mario.
        It will be used to make Mario lose lives'''
        onlyonce = False
        for el in range (self.x, self.x + 12):
            if el in range (xMario, xMario + 12):
                for el in range (self.y, self.y + 10):
                    if el in range (yMario, yMario + 16):
                        onlyonce = True  
        if onlyonce and self.__notDone:
            self.__notDone = False
            return True
        elif not onlyonce:
            self.__notDone = True
            return False
    
    
    def win_points (self, xMario: int, yMario: int, jumpingMario: bool):
        '''Returns a boolean that checks if Mario is in a certain range upper
        the barrel and if is jumping to win the 100 points given for jumping a barrel'''
        is_over_barrel= False
        for var in range (self.x, self.x + 12):
            if var in range (xMario, xMario + 12):
                for var in range (self.y-30, self.y - 1):
                    if var in range (yMario, yMario + 16):
                        is_over_barrel = True  
        if is_over_barrel and self.__notRevised and jumpingMario:
            self.__notRevised = False
            return True
        elif not is_over_barrel:
            self.__notRevised = True
            return False
        
