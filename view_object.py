from direct.showbase.ShowBase import ShowBase
from panda3d.core import Texture
from pubsub import pub


class ViewObject:
    def __init__(self, game_object):
        self.game_object = game_object
        self.cube = base.loader.loadModel("models/cube")
        self.cube.reparentTo(base.render)
        self.cube.setPos(*game_object.position)
        self.cube.setScale(1, 1, 1)
        self.cube_texture = base.loader.loadTexture("textures/crate.png")
        self.cube.setTexture(self.cube_texture)
        self.cube.setTag('selectable', '')
        self.cube.setPythonTag("owner", self)
        self.is_selected = False
        self.texture_on = True
        self.toggle_texture_pressed = False

        pub.subscribe(self.toggle_texture, 'input')

    def toggle_texture(self, events=None):
        if 'toggleTexture' in events:
            self.toggle_texture_pressed = True

    def selected(self):
        self.is_selected = True

    def tick(self):
        if (self.toggle_texture_pressed):
                #and self.is_selected):
            if self.texture_on:
                self.texture_on = False
                self.cube.setTextureOff(1)
            else:
                self.texture_on = True
                self.cube.setTexture(self.cube_texture)
            self.toggle_texture_pressed = False

        self.is_selected = False
