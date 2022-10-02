
class DonkeyKong:
    '''This class will be initialized as an object only once, as well as Mario
    and Pauline. In this class we will also create an attribute that controls if
    Donkey Kong is throwing a barrel, a value that will be used for animating
    him taking barrels and throwing them.'''
    
    def __init__ (self, x: int, y: int):
        '''This method initializes the DonkeyKong object'''
        self.x = x
        self.y = y
        self.throwingBarrel = False
        self.direction = -43
    
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
    def throwingBarrel (self):
        return self.__throwingBarrel
    @throwingBarrel.setter
    def throwingBarrel (self, throwingBarrel):
        self.__throwingBarrel = throwingBarrel
            

        
        
   

