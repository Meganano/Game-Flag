import arcade.key

HIT_SIZE_WIDTH = 25
HIT_SIZE_HEIGHT = 50
HIT_SIZE_PLAYER = 32

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.player1 = Player1(self,150, 250)
        self.player2 = Player2(self,650,250)
        self.flag_p1 = FlagPlayer1(self,50,270)
        self.flag_p2 = FlagPlayer2(self,750,270)
        
    def on_key_press(self, key, key_modifiers):
        ##try to use array
        self.player2.directions_press(key,key_modifiers)
        self.player1.directions_press(key,key_modifiers)

        
    def on_key_release(self, key, key_modifiers):
        self.player2.directions_release(key,key_modifiers)
        self.player1.directions_release(key,key_modifiers)
        
    def update(self, delta):
            self.player1.update(delta)
            self.player2.update(delta)
            self.flag_p1.update(delta)       
            self.flag_p2.update(delta)

class FlagPlayer1:
    def __init__(self,world,x,y):
        self.world = world
        self.x = x
        self.y = y
        self.getflag = False
        
    def update(self,delta):
        ##print("self.x:",self.x)
        ##print("self.y:",self.y)
        if (abs(self.x - self.world.player2.x) <= HIT_SIZE_WIDTH) and (abs(self.y - self.world.player2.y) <= HIT_SIZE_HEIGHT):
            self.x = self.world.player2.x
            self.y = self.world.player2.y
            self.getflag = True
        if(abs(self.world.player1.x - self.world.player2.x) <= HIT_SIZE_PLAYER) and (abs(self.world.player1.y - self.world.player2.y) <= HIT_SIZE_PLAYER) and (self.getflag == True):
            self.x = 50
            self.y = 270
            self.getflag = False

class Player2:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.direction2 = []

    def directions_press(self, key,key_modifiers):
        if key == arcade.key.UP:
            self.direction2.append('up')
        if key == arcade.key.DOWN:
            self.direction2.append('down')
        if key == arcade.key.LEFT:
             self.direction2.append('left')
        if key == arcade.key.RIGHT:
            self.direction2.append('right')

    def directions_release(self,key,key_modifiers):
        if key == arcade.key.UP:
            self.direction2.remove('up')
        if key == arcade.key.DOWN:
            self.direction2.remove('down')
        if key == arcade.key.LEFT:
             self.direction2.remove('left')
        if key == arcade.key.RIGHT:
            self.direction2.remove('right')
            
    def update(self, delta):
        for i in range(len(self.direction2)):
            if self.direction2[i] != '\n':
                if self.direction2[i] == 'up' and self.y < self.world.height:
                    self.y += 5
                if self.direction2[i] == 'down' and self.y > 0:
                    self.y -= 5
                if self.direction2[i] == 'right' and self.x < self.world.width:
                   self.x += 5
                if self.direction2[i] == 'left' and self.x > 0:
                   self.x -= 5
        

class FlagPlayer2:
    def __init__(self,world,x,y):
        self.world = world
        self.x = x
        self.y = y
        self.getflag = False
        
    def update(self,delta):
        ##print("self.x:",self.x)
        ##print("self.y:",self.y)
        if (abs(self.x - self.world.player1.x) <= HIT_SIZE_WIDTH) and (abs(self.y - self.world.player1.y) <= HIT_SIZE_HEIGHT):
            self.x = self.world.player1.x
            self.y = self.world.player1.y
            self.getflag = True
        if(abs(self.world.player1.x - self.world.player2.x) <= HIT_SIZE_PLAYER) and (abs(self.world.player1.y - self.world.player2.y) <= HIT_SIZE_PLAYER) and (self.getflag == True):
            self.x = 750
            self.y = 270
            self.getflag = False

        
class Player1:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.directions1 = []


    def directions_press(self, key,key_modifiers):
        if key == arcade.key.W:
            self.directions1.append('up')
        if key == arcade.key.S:
            self.directions1.append('down')
        if key == arcade.key.A:
             self.directions1.append('left')
        if key == arcade.key.D:
            self.directions1.append('right')

    def directions_release(self,key,key_modifiers):
        if key == arcade.key.W:
            self.directions1.remove('up')
        if key == arcade.key.S:
            self.directions1.remove('down')
        if key == arcade.key.A:
             self.directions1.remove('left')
        if key == arcade.key.D:
            self.directions1.remove('right')
    
    def update(self, delta):  
        for i in range(len(self.directions1)):
            if self.directions1[i] != '\n':
                if self.directions1[i] == 'up' and self.y < self.world.height:
                    self.y += 5
                if self.directions1[i] == 'down' and self.y > 0:
                    self.y -= 5
                if self.directions1[i] == 'right' and self.x < self.world.width:
                   self.x += 5
                if self.directions1[i] == 'left' and self.x > 0:
                   self.x -= 5
