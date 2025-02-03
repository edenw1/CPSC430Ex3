
class ViewObject:
    def __init__(self, game_object):
        self.game_object = game_object
        self.cube = base.loader.loadModel("models/cube")
        self.cube.reparentTo(base.render)
        self.cube.setPos(*game_object.position)
        self.cube.setScale(1, 1, 1)
        cube_texture = base.loader.loadTexture("textures/crate.png")
        self.cube.setTexture(cube_texture)

    def tick(self):
        pass
