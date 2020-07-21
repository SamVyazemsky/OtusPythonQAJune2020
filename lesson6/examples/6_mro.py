class A:
    def get_name(self):
        print('This is class A')


class B:
    def get_name(self):
        print('This is class B')


class C(A, B):
    pass


class D(C):
    def get_name(self):
        print('This is class D')


class F(D, C):
    def get_name_class(self):
        print('this is class F')


print(F.mro())

d = F()
d.get_name()
