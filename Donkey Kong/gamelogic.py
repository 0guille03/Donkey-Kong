
import pyxel
import random
import constants
#Importing from objects 
from mario import Mario
from pauline import Pauline
from donkeykong import DonkeyKong
from barrels import Barrels
from staticsprite import StaticSprite


class Game:
    '''The class game is the base of the rest of the classes because is where the rest
    of the classes will be used as objects. In this class we will have functions related
    to the general ejecution of the game like the function update or restart. 
    Also all the commands ralated with Pyxel are in this class '''
    
    def __init__ (self):
        ''' This method initialices the game ''' 
        #Create Objects as attributes
        self.mario = Mario (constants.X_MARIO, constants.Y_MARIO, constants.LIVES, constants.POINTS)
        self.pauline = Pauline (constants.X_PAULINE, constants.Y_PAULINE)
        self.donkeyKong = DonkeyKong (constants.X_DONKEYKONG, constants.Y_DONKEYKONG)
        self.staticsprite = StaticSprite()
        #Create list where barrell objects will be stored        
        self.blist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        #Attributes that determine the status of the game
        self.loose = False
        self.win = False
        
        self.canThrowBarrel = False
        self.timeThrowingBarrel = 0
        #Initialice pyxel
        pyxel.init(constants.WIDTH, constants.HEIGHT, caption=constants.CAPTION)
        pyxel.load("finals.pyxres")
        pyxel.run(self.update, self.draw)
        
        
    def update(self):
        ''' This method is executed every frame. Here it controls each botton pressed
        and functions need the to work all the time'''
        if pyxel.btnp(pyxel.KEY_Q): #Q to quit game
            pyxel.quit()     
        if not self.loose and not self.win:
            self.all_barrels()
            self.move_mario()
            self.mario.check_all_time(self.staticsprite.board) 
            #Function in mario object that needs to be run every frame
            
            #Check if reach the goal
            if self.pauline.touchmario(self.mario.x,self.mario.y):
               self.win=True
            
            
    def draw(self):
        ''' This method draws graphics from the image bank'''
        pyxel.cls(0)
        #Printing Pauline
        pyxel.blt(self.pauline.x, self.pauline.y, 2, 0, 0, 16, 23,colkey=0)
        #Printing Donkey Kong and its movements
        if self.donkeyKong.throwingBarrel:
            pyxel.blt(self.donkeyKong.x, self.donkeyKong.y, 1, 0, 48, self.donkeyKong.direction, 32,colkey=0) 
        else:
            pyxel.blt(self.donkeyKong.x, self.donkeyKong.y, 1, 0, 16, 40, 32,colkey=0) 
        # the static components on screen (barrels and ladders)
        for j in range (len (self.staticsprite.board)):
            for i in range (len (self.staticsprite.board[j])):
                #Printing platforms
                if self.staticsprite.board[j][i] == 1 and i%16 == 0:
                    pyxel.blt (i, j, 0, 32, 40, 16, 8,colkey=0)  
                #Printing ladders
                if self.staticsprite.board[j][i] in range (2, 4) and i%8 == 0 and j%8 == 0:
                    pyxel.blt (i, j, 0, 16, 40, 8, 8,colkey=0)
        #Printing barrels on screen
        for el in range (10):
            if self.blist[el] != 0:
                if self.blist[el].isGoingDown:
                    pyxel.blt(self.blist[el].x, self.blist[el].y, 0, 0, 86, 12, 10,colkey=0) #Barrel going down a ladder
                else:
                    pyxel.blt(self.blist[el].x, self.blist[el].y, 0, 0, 38, 12, 10,colkey=0) #Barrel the rest of the time
        #Printing Mario's lives on screen
        for el in range (self.mario.lives):
            pyxel.blt(198-el*18, 0, 2, 16, 0, 16, 16,colkey=0)
        #Printing Mario's points on screen    
        pyxel.text(180, 18,"Point:%s" %str(self.mario.points), pyxel.frame_count % 16)
        #Printing Mario on screen 
        pyxel.blt(self.mario.x, self.mario.y, 1, 0, 0, self.mario.direction, 16,colkey=0)
        #Printing text when the game has ended
        if self.loose:
            pyxel.text(constants.WIDTH/2- 20, constants.HEIGHT/2 -15, "GAME OVER", pyxel.frame_count % 16)   
        if self.win:
            pyxel.text(constants.WIDTH/2- 40, constants.HEIGHT/2 -15 , "      YOU WON\nYour score:%s Points"%str(self.mario.points), pyxel.frame_count % 16)
        
        
    def move_mario (self):
        '''This method controlls the movements of Mario when commanded by keyboard'''
        #checks if conditions sarisfied for Mario to jump
        if pyxel.btnp(pyxel.KEY_SPACE) and self.mario.touching_floor(self.staticsprite.board): 
            self.mario.canJump = True 
        #Here it allows mario to move horizontally untill the border is reached
        elif pyxel.btn(pyxel.KEY_RIGHT) and self.mario.x + 11 in range (constants.WIDTH-1):
            self.mario.move ("right")            
        elif pyxel.btn(pyxel.KEY_LEFT) and self.mario.x - 1 in range (constants.WIDTH-1):
            self.mario.move ("left")
        #It check if mario is touching a ladder and allows him to go up and down.            
        elif pyxel.btn(pyxel.KEY_UP) and self.mario.touching_ladder_up(self.staticsprite.board):
            self.mario.move ("up")            
        elif pyxel.btn(pyxel.KEY_DOWN) and self.mario.touching_ladder_down(self.staticsprite.board):
            self.mario.move ("down")            

            
    def all_barrels (self):
        '''This method checks fills the barrel list and controlls what they do'''
        self.animation_throw_barrel() #This method iniciates the barrels
        #Making barrels move and deleting them when they reach the end.
        for el in range (10):
            if self.blist[el] != 0:
                self.blist[el].move(self.staticsprite.board)
                if self.blist[el].y in range (230, 248) and self.blist[el].x in range (0,2):
                    self.blist[el] = 0
        #Here we sum points to mario        
        for el in range (10):
            if self.blist[el] != 0:
                if self.blist[el].win_points(self.mario.x, self.mario.y, self.mario.jumping):
                    self.mario.points += 100
        #Checking if a barrel is touching Mario to make him loose a live, and restart when all lives are lost
        for el in range (10):
            if self.blist[el] != 0:
                if self.blist[el].touching_mario(self.mario.x, self.mario.y):
                    self.mario.lives -= 1
                    if self.mario.points != 0 and self.mario.jumping:
                        self.mario.points -= 100
                    if self.mario.lives == 0:
                        self.loose = True
                    else:
                        self.restart()  
                        
                        
    def animation_throw_barrel (self):
        '''This part fills the barrel list randomly which makes the appear. And also makes the Donkey kong move before throwing it'''
        if (pyxel.frame_count)%50 == 0 and (random.randrange(1, 4) == 3) and 0 in self.blist: 
            self.canThrowBarrel = True         
        if self.canThrowBarrel:
            self.timeThrowingBarrel += 1
            if self.timeThrowingBarrel <= 15:
                self.donkeyKong.throwingBarrel = True
                self.donkeyKong.direction = 43
            elif self.timeThrowingBarrel == 50:
                #Creating barrel, only one at a time
                for var in range (10):
                    if self.blist[var] == 0 and self.canThrowBarrel:
                        self.blist[var] = Barrels(constants.X_BARRELS, constants.Y_BARRELS)
                        self.canThrowBarrel = False
                self.donkeyKong.throwingBarrel = False  
                self.donkeyKong.direction = 40
                self.timeThrowingBarrel = 0
            elif self.timeThrowingBarrel > 30:
                self.donkeyKong.throwingBarrel = True
                self.donkeyKong.direction = -43
            else:
                self.donkeyKong.throwingBarrel = False
                self.donkeyKong.direction = 40
            
            
    def restart(self):
        '''This function restarts the game when a life is lost'''
        self.mario = Mario (constants.X_MARIO, constants.Y_MARIO, self.mario.lives, self.mario.points)
        self.blist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

      


Game()
