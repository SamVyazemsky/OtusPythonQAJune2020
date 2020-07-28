from abc import ABC, abstractmethod


class Opener(ABC):

    @property
    @abstractmethod
    def material(self):
        pass

    @abstractmethod
    def open(self):
        return NotImplemented

class Closer(ABC):

    @abstractmethod
    def close(self):
        return NotImplemented


class Door(Opener, Closer):
    material = None

    def __init__(self, material):
        self.material = material

    def close(self):
        print(f"{self.material} door is closed!")

    # def open(self):
    #     print(f"{self.material} door is  opened!")


glass_door = Door(material="Glass")
# glass_door.open()
# glass_door.close()
