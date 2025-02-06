from direct.showbase.ShowBase import ShowBase
from direct.task import Task
import sys

from panda3d.core import CollisionTraverser, CollisionHandlerQueue, CollisionRay, GeomNode, CollisionNode
from pubsub import pub

from game_logic import GameLogic
from player_view import PlayerView

controls = {
    'w': 'forward',
    'a': 'left',
    's': 'backward',
    'd': 'right',
    'q': 'toggleTexture'
}

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
        picker_node = CollisionNode('mouseRay')
        picker_np = self.camera.attachNewNode(picker_node)
        picker_node.setFromCollideMask(GeomNode.getDefaultCollideMask())
        self.pickerRay = CollisionRay()
        picker_node.addSolid(self.pickerRay)
        picker_np.show()
        self.rayQueue = CollisionHandlerQueue()
        self.cTrav = CollisionTraverser()
        self.cTrav.addCollider(picker_np, self.rayQueue)
        self.taskMgr.add(self.tick)
        self.input_events = {}
        for key in controls:
            self.accept(key, self.input_event, [controls[key]])
        self.run()

    def get_nearest_object(self):
        self.pickerRay.setFromLens(self.camera, 0, 0)
        if self.rayQueue.getNumEntries() > 0:
            self.rayQueue.sortEntries()
            entry = self.rayQueue.getEntry(0)
            picked_np = entry.getIntoNodePath()
            picked_np = picked_np.findNetTag('selectable')
            if not picked_np.isEmpty() and picked_np.getPythonTag("owner"):
                return picked_np.getPythonTag("owner")
        return None

    def input_event(self, event):
        self.input_events[event] = True

    def tick(self, task):
        pub.sendMessage('input', events=self.input_events)
        self.game_logic.tick()
        self.player_view.tick()
        if self.game_logic.get_property("quit"):
            sys.exit()
        self.input_events.clear()
        return Task.cont

if __name__ == '__main__':
    main = Main()
    main.go()
