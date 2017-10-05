class Player1:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    def update(self, delta):
        if self.y > 500:
            self.y = 500
        self.y += 5
