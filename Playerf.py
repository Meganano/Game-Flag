import arcade.key

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
 
        self.player1 = Player1(self,150, 250)
        self.player2 = Player2(self,650,250)
 
    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.UP:
            self.player1.switch_up()
        if key == arcade.key.DOWN:
            self.player1.switch_down()
        if key == arcade.key.LEFT:
            self.player1.switch_left()
        if key == arcade.key.RIGHT:
            self.player1.switch_right()

        if key == arcade.key.W:
            self.player2.switch_up()
        if key == arcade.key.S:
            self.player2.switch_down()
        if key == arcade.key.A:
            self.player2.switch_left()
        if key == arcade.key.D:
            self.player2.switch_right()

    def update(self, delta):
        self.player1.update(delta)
        self.player2.update(delta)


class Player2:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

    def switch_up(self):
        self.y += 5
    def switch_down(self):
        self.y -= 5
    def switch_right(self):
        self.x += 5
    def switch_left(self):
        self.x -= 5
            
    def update(self, delta):
        if self.y > self.world.height:
            self.y = self.world.height
        if self.y < 0:
            self.y = 0
        if self.x < 0:
            self.x = 0
        if self.x > self.world.width:
            self.x = self.world.width

class Player1:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

    def switch_up(self):
        self.y += 5
    def switch_down(self):
        self.y -= 5
    def switch_right(self):
        self.x += 5
    def switch_left(self):
        self.x -= 5
            
    def update(self, delta):
        if self.y > self.world.height:
            self.y = self.world.height
        if self.y < 0:
            self.y = 0
        if self.x < 0:
            self.x = 0
        if self.x > self.world.width:
            self.x = self.world.width
        
