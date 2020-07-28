class Numbers:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def increase_sum(self):
        return (self.a + self.b) * 10

    def sum(self):
        return self.a + self.b

    def diff(self):
        return self.a - self.b

    def multi(self):
        return self.a * self.b

    def devision(self):
        return self.a // self.b

    def mod(self):
        return self.a % self.b

