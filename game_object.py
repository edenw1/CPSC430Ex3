class GameObject:
    def __init__(self, position, kind, id):
        self.position = position
        self.kind = kind
        #crate, wall
        self.id = id
        #id for if there are multiple of those objects

    def tick(self):
        pass
