
class Mario:
    '''This class will be used as an object only once (because we only have one
    Mario). Here we define the movement of Mario and his interaction with static
    elements of the board (which are the ones that let him move in different ways).
    Some of the methods of this class have big similarities with the ones that appear
    in the class barrels because funtions like fall do exactly the same in both cases'''    
    
    def __init__ (self, x: int, y: int, lives: int, points: int):
        '''This method initializes the Mario object'''
        #atributes shown in game
        self.x = x
        self.y = y
        self.lives = lives        
        self.points = points
        #atributes used in gamelogic
        self.direction = 12
        self.canJump = False
        self.jumping = False #True when mario is jumping      
        #atributes not needed out of this object
        self.__falling = True #True when mario is falling
        self.__timeJumping = 0
        
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
    def lives (self):
        return self.__lives 
    @lives.setter
    def lives (self, lives):
        self.__lives = lives
    
    @property
    def points(self):
        return self.__points    
    @points.setter
    def points (self, points):
        self.__points = points  
        
    @property
    def jumping(self):
        return self.__jumping   
    @jumping.setter
    def jumping (self, jumping):
        self.__jumping = jumping
        
        
    
    def check_all_time(self, board: list):
        '''This method checks all the Mario methods that need to be checked every
        frame'''
        self.can_jump()
        self.fall(board)
        
        
    def move (self, d: str):
        '''This method is in charge of the movements mario makes (left, right or up or
        down a ladder). d is the direction given by the pressed Key'''
        if d == "right" :
            self.x += 1
            self.direction = 12 #To change Mario's direction
        elif d == "left":
            self.x -= 1
            self.direction = -12
        elif d == "up" and not self.jumping:
            self.y -= 1 #when you go up you reach 0 so num decrease
        elif d == "down" and not self.jumping:
            self.y += 1
            
            
    def can_jump(self):
        '''This method checks if the conditions so if they are satisfied Mario can
        jump'''
        if self.canJump:
            if self.__timeJumping < 15: #This condition makes mario jump during 15 frames
                self.__timeJumping += 1
                self.jumping = True
                if self.__timeJumping <= 9: #It only goes up the first nine frames
                    self.y -= 2
                if self.__timeJumping == 14: #At 14 frames the jump ends
                    self.jumping = False 
                    self.canJump= False #Restart the condition that allows him to jump
                    self.__timeJumping = 0 #Restart the time for next jump
                
                
    def fall (self, board: list):
        '''This method makes mario fall if he isn't touching the floor'''
        if not self.touching_floor(board) and not self.touching_ladder_down(board) and not self.touching_ladder_up(board) and not self.jumping:
            self.y +=1
            self.__falling = True 
        else:
            self.__falling = False
            
            
    def touching_ladder_down(self, board: list):
        '''This method checks conditions needed for mario to go down a ladder'''
        if (board [self.y + 16][self.x + 6] == 2 or board [self.y + 24][self.x + 6] == 2) and board[self.y + 7][self.x + 6] != 3 and not self.jumping and not self.__falling:
            return True
        else:
            return False
        
        
    def touching_ladder_up(self, board: list):
        '''This method checks conditions needed for mario to go up a ladder'''
        if (board [self.y + 14][self.x + 6] == 2 or board [self.y + 23][self.x + 6] == 2) and board[self.y + 7][self.x + 6] != 3 and not self.jumping and not self.__falling:
            return True
        else:
            return False
        
        
    def touching_floor (self, board: list):
        '''This method check if mario is touching the floor'''
        if board [self.y +16][self.x + 6] == 1:
            return True
        else:
            return False
