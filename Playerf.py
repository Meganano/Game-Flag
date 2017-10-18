import arcade.key

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.player1 = Player1(self,150, 250)
        self.player2 = Player2(self,650,250)
        

    def on_key_press(self, key, key_modifiers):
        ##try to use array
        if key == arcade.key.UP:
            self.player2.directions('up')
        if key == arcade.key.DOWN:
            self.player2.directions('down')
        if key == arcade.key.LEFT:
            self.player2.directions('left')
        if key == arcade.key.RIGHT:
            self.player2.directions('right')

        if key == arcade.key.W:
            self.player1.directions('w')
        if key == arcade.key.S:
            self.player1.directions('s')
        if key == arcade.key.A:
            self.player1.directions('a')
        if key == arcade.key.D:
            self.player1.directions('d')
            
    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.W or key == arcade.key.S or key == arcade.key.A or key == arcade.key.D:
            self.player1.directions('\n')
        if key==arcade.key.UP or key==arcade.key.DOWN or key==arcade.key.RIGHT or key == arcade.key.LEFT:
            self.player2.directions('\n')
    
    def update(self, delta):
            self.player1.update(delta)
            self.player2.update(delta)


class Player2:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.key = '\n'

    def directions(self, key):
        self.key = key
            
    def update(self, delta):
        if self.key != '\n':
            if self.key == 'up' and self.y < self.world.height:
                self.y += 5
            if self.key == 'down' and self.y > 0:
                self.y -= 5
            if self.key == 'right' and self.x < self.world.width:
               self.x += 5
            if self.key == 'left' and self.x > 0:
               self.x -= 5
               

class Player1:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.key = '\n'


    def directions(self, key):
        self.key = key
            
    def update(self, delta):
        if self.key != '\n':
            if self.key == 'w' and self.y < self.world.height:
                self.y += 5
            if self.key == 's' and self.y > 0:
                self.y -= 5
            if self.key == 'd' and self.x < self.world.width:
               self.x += 5
            if self.key == 'a' and self.x > 0:
               self.x -= 5
