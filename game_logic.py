from game_object import GameObject
from pubsub import pub

class GameLogic:
    def __init__(self):
        self.properties = {}
        self.game_objects = {}
        self.next_id = 0

    def create_object(self, position, kind):
        obj = GameObject(position, kind, self.next_id)
        self.game_objects[obj.id] = obj
        self.next_id += 1
        pub.sendMessage('create', game_object=obj)
        return obj

    def tick(self):
        for id in self.game_objects:
            self.game_objects[id].tick()

    def load_world(self):
        self.create_object([0, 0, 0], "crate")

    def get_property(self, key):
        if key in self.properties:
            return self.properties[key]
        return None

    def set_property(self, key, value):
        self.properties[key] = value
