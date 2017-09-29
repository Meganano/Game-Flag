import arcade
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

class MyApplication(arcade.Window):
    def __init__(self, width, height):
        
        # Call the parent class initializer
        super().__init__(width, height)

        # Background image will be stored in this variable
    ##    self.background = None

        # Set the background color
        arcade.set_background_color(arcade.color.BLUE)

    def setup(self):
        """ Set up the game and initialize the variables. """
        self.background = arcade.load_texture("images/space-bg.jpg")

    def on_draw(self):
        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw the background texture
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)


def main():
    """ Main method """
    window = MyApplication(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
