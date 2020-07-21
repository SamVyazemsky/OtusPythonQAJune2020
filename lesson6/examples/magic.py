class Magic:

    def __init__(self, count):
        self.count = count

    # def __repr__(self):
    #     return "***Magic***"

    # def __str__(self):
    #     return "***Magic***"

    #
    def __add__(self, other):
        return str(self) + " **** and ***** " + str(other)
    #
    # #
    # def __eq__(self, other):
    #     return self.count == other.count
    #
    # def __call__(self, *args):
    #     return str(self) + " got args " + str(args)


# str
b1 = Magic(100)
b2 = Magic(200)

# print(b1)
# print(b2)

# add
# print(str(b1) + str(b2))
print(b1+b2)

# print(b1 == b2)
