import arcade.key

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
 
        self.player1 = Player1(self,150, 250)
 
    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.UP:
            self.player1.switch_up()
        if key == arcade.key.DOWN:
            self.player1.switch_down()
        if key == arcade.key.LEFT:
            self.player1.switch_left()
        if key == arcade.key.RIGHT:
            self.player1.switch_right()

    def update(self, delta):
        self.player1.update(delta)


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
        
