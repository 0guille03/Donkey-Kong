
import constants

class StaticSprite:
    '''This class contains every element of the game that is static which are ladders
    and  platforms. In this class a matrix board will be created to be used as a
    reference of the position of all the objects of the program. Quite a few
    methods of the game use this board'''
    
    def __init__ (self):
        '''This is a function to create a matrix with 1 where ladders are be and 2 and 3 where stairs  are'''
        #Creation of the matrix for the static part (ladders and platforms)
        self.board = []
        
        listPLeft = [48, 128, 208] #y of platforms with hole in right
        listPRight = [88, 168] #y of platforms with hole in left
        #this for is for generating a list with 0 (nothing) and 1 (plataforms)
        for y in range (constants.HEIGHT+13): 
            list1 = []
            for x in range (constants.WIDTH ):
                if y == 24 and x in range (48,128):
                    list1.append (1) 
                elif y == 248:
                    list1.append (1)
                elif y in listPLeft and x < constants.WIDTH - 32:
                    list1.append (1)    
                elif y in listPRight and x >= 32:
                    list1.append (1)    
                else:
                    list1.append (0)
            self.board.append(list1)
        #Filling some 0 (nothing) with a 2 or 3 (ladders)
        for y in range (len (self.board) ): 
            for x in range (len (self.board[y])):
                #usefull ladders 
                if y in range (32,48) and x in range (104,112):
                    self.board[y][x] = 2
                elif x in range(168, 176) and (y in range (216, 248) or y in range (136, 168) or y in range (56, 88)):
                    self.board[y][x] = 2
                elif x in range(48, 56) and (y in range (176, 208) or y in range (96, 128)):
                    self.board[y][x] = 2   
                #useless ladders
                elif y in range (56, 64) and x in range (64, 72):
                    self.board[y][x] = 3  
                elif y in range (136, 152) and x in range (88, 96):
                    self.board[y][x] = 3                    
                elif y in range (176, 184) and x in range (152, 160):
                    self.board[y][x] = 3                    
                elif y in range (216, 224) and x in range (74, 88):
                    self.board[y][x] = 3                      
                elif y in range (72, 88) and x in range (64, 72):
                    self.board[y][x] = 2                    
                elif y in range (160, 168) and x in range (88, 96):
                    self.board[y][x] = 2                    
                elif y in range (200, 208) and x in range (152, 160):
                    self.board[y][x] = 2                    
                elif y in range (240, 248) and x in range (74, 88):
                    self.board[y][x] = 2                     

