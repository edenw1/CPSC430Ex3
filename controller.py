from direct.showbase.ShowBase import ShowBase
from direct.task import Task
import sys

from game_logic import GameLogic
from player_view import PlayerView

class Main(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.disableMouse()
        self.render.setShaderAuto()

        self.game_logic = GameLogic()
        self.player_view = PlayerView(self.game_logic)

    def go(self):
        self.game_logic.load_world()
        self.camera.set_pos(0, -20, 0)
        self.camera.look_at(0, 0, 0)
        self.taskMgr.add(self.tick)
        self.run()

    def tick(self, task):
        self.game_logic.tick()
        self.player_view.tick()
        if self.game_logic.get_property("quit"):
            sys.exit()
        return Task.cont

if __name__ == '__main__':
    main = Main()
    main.go()
