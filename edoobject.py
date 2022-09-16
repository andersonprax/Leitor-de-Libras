class EdoObject:
    def __init__(self):
        self.name = None
        self.handle = None
        self.pos = 0
        self.rel_pos = 0
        self.type = ''
        self.orient = None
        self.vel = None
        self.init_pos = None


    def dict_sim(self):
        return {'Position': self.rel_pos, 'Velocity': self.vel, 'Current': None,
                'carteseanPosition': self.pos}

    def dict(self):
        return {'name': self.name, 'handle': self.handle, 'pos': self.pos,
                'rel_pos': self.rel_pos, 'orientation': self.orient, 'velocity': None}

    def show(self, replace=True):
        if replace:
            print(f'\r{self.dict()}')
        else:
            print(self.dict())
