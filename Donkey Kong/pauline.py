
class Pauline:
    '''This class is only used as an object once as well and is used to create Pauline.
    It's main purpose is to check if is in contact with Mario and let the player
    win the game.'''
    
    def __init__ (self, x: int, y: int):
        '''This function initializes the position of the Pauline object and 
        if she is touching Mario'''
        self.x = x
        self.y = y
        self.touchingmario = False
     
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
    def touchingmario(self):
        return self.__touchingmario
    @touchingmario.setter
    def touchingmario (self, touchingmario):
        self.__touchingmario = touchingmario    
    
        
    def touchmario (self, xMario: int, yMario: int):
        '''This method checks if Mario is at Pauline's possition'''
        for el in range (self.x, self.x + 16):
            if el in range (xMario, xMario + 12):
                for el in range (self.y, self.y + 15):
                    if el in range (yMario, yMario + 16):
                        return True  

        
        
