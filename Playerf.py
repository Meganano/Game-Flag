class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
 
        self.player1 = Player1(self,150, 250)
 
 
    def update(self, delta):
        self.player1.update(delta)


class Player1:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
 
    def update(self, delta):
        if self.y > self.world.height:
            self.y = self.world.height
        self.y += 5
