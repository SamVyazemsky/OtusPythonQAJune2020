class Car:
    # incapsulation (private,protected)
    # getter,setter

    __color = 'white'
    _wheel = 4

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    engine_status = 'off'

    def __protected_method(self):
        print('protected')

    def get_color(self):
        print(self.__color)

    def set_color(self, new_color):
        if new_color not in ['black', 'red', 'green']:
            self.__color = new_color
        print(self.__color)

    def start_engine(self):
        self.engine_status = 'on'
        print(f'{self.brand} {self.model} engine car is starting')

    def run(self):
        if self.engine_status == 'off':
            self.start_engine()
            print(f'{self.brand} {self.brand} car is running')
        else:
            print(f'{self.brand} {self.brand} car engine is  already running')

    def off_engine(self):
        if self.engine_status == 'on':
            print(f'{self.brand} {self.model} engine car is turn off')
        else:
            print('car engine is already turn off')


# Car.__color = 'test'
toyota = Car('Toyota', 'camry')
print(toyota._wheel)
# print(toyota.get_color())
# print(toyota.__color)
# toyota.get_color()


# print(toyota._Car__color)
# toyota.start_engine()
# toyota.get_color()

toyota.set_color('blue')

# print(dir(toyota))
