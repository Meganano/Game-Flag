import arcade
from Playerf import World

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500


class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
        super().__init__(*args, **kwargs)
 
    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
 
    def draw(self):
        self.sync_with_model()
        super().draw()

class MyApplication(arcade.Window):
    def __init__(self, width, height):       
        super().__init__(width, height)
        self.world = World(width,height)
        

    def setup(self):
        """ Set up the game and initialize the variables. """
        self.background = arcade.load_texture("images/space-bg.jpg")

        self.player1_p = ModelSprite('images/Player1.png',model=self.world.player1)        
        
        self.player2_p = ModelSprite('images/Player2.png',model=self.world.player2)
        
        self.town1 = arcade.Sprite('images/town1.png')
        self.town1.set_position(50,270)
        
        self.town2 = arcade.Sprite('images/town2.png')
        self.town2.set_position(750,270)
        
        self.flag1 = arcade.Sprite('images/flag1.png')
        self.flag1.set_position(50,270)
        
        self.flag2 = arcade.Sprite('images/flag2.png')
        self.flag2.set_position(750,270)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.player1_p.draw()
        self.player2_p.draw()
        self.town1.draw()
        self.town2.draw()
        self.flag1.draw()
        self.flag2.draw()

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

    def on_key_release(self, key, key_modifiers):
        self.world.on_key_release(key, key_modifiers)

    def update(self, delta):
        self.world.update(delta)


def main():
    window = MyApplication(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
