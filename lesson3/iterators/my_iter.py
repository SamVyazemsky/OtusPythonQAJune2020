class MyIterator:
    def __init__(self, val):
        self.val = val

    def __iter__(self):
        self.n = self.val
        return self

    def __next__(self):
        new = self.n
        self.n += 2
        if self.n > 1000:
            raise StopIteration
        return new


it = MyIterator(1)
for i in it:
    print(i)
