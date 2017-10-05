import arcade
from firstplayer import Player1

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

class MyApplication(arcade.Window):
    def __init__(self, width, height):       
        # Call the parent class initializer
        super().__init__(width, height)


    def setup(self):
        """ Set up the game and initialize the variables. """
        self.background = arcade.load_texture("images/space-bg.jpg")

        self.player1 = Player1(150,250)
        self.player1_model = arcade.Sprite('images/Player1.png')
        #self.player1.set_position(150,250)
        
        self.player2 = arcade.Sprite('images/Player2.png')
        self.town1 = arcade.Sprite('images/town1.png')
        self.town2 = arcade.Sprite('images/town2.png')
        self.flag1 = arcade.Sprite('images/flag1.png')
        self.flag2 = arcade.Sprite('images/flag2.png')
        
        self.player2.set_position(650,250)
        self.town1.set_position(50,270)
        self.town2.set_position(750,270)
        self.flag1.set_position(50,270)
        self.flag2.set_position(750,270)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        self.player1_model.draw()
        
        self.player2.draw()
        self.town1.draw()
        self.town2.draw()
        self.flag1.draw()
        self.flag2.draw()
        
    def update(self, delta):
        player1 = self.player1

        player1.update(delta) 
        self.player1_model.set_position(player1.x, player1.y + 5)



def main():
    window = MyApplication(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
