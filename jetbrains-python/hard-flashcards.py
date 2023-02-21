class Animal:
    def __init__(self, name):
        self.name = name
    

class Bird(Animal):
    def __repr__(self):
        return self.name
    

class Pigeon(Bird):
    def __repr__(self):
        return self.name


class Sparrow(Bird):
    def __repr__(self):
        return self.name
    