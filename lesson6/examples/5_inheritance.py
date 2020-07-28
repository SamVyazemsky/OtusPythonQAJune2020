class Vehicle:
    # наследование и полиморфизм
    # __color = 'white'
    # _wheel = 4
    __engine_status = 'off'

    def __init__(self, brand, model, wheels):
        self.brand = brand
        self.model = model
        self.color = wheels

    def get_engine_status(self):
        return self.__engine_status

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
        self.start_engine()
        print(f'{self.brand} {self.brand} car is running')

    def off_engine(self):
        if self.engine_status == 'on':
            print(f'{self.brand} {self.model} engine car is turn off')
        else:
            print('car engine is already turn off')


class Sport:
    def __init__(self, speed):
        self.speed = speed

    def fast_start(self):
        print('car realized fast start')


class Car(Vehicle):
    # __color = 'white'
    # _wheel = 4

    def __init__(self, brand, model):
        # super().__init__(brand, model, wheels)
        # self.speed = speed
        super().__init__(brand, model, 4)

    def get_property(self):
        print('Iam car')


class Moto(Vehicle):
    def __init__(self, brand, model):
        # super().__init__(brand, model, wheels)
        super().__init__(brand, model, 2)

    def run(self):
        if self.get_engine_status() != 'on':
            self.start_engine()
            print(f'engine status of moto {self.brand} {self.model} is on')
        else:
            print(f'moto {self.brand} {self.model} is running')


# toyota = Car(brand='toyota', model='camry')
# moto = Moto(brand='bmw', model='Adventure', wheels=10)


# toyota = Car(brand='toyota', model='camry')
# toyota.run()

# moto = Moto(brand='bmw', model='Adventure')
# moto.run()

# Подклассы
# print(issubclass(Moto, Vehicle))
# print(issubclass(Vehicle, Moto))

# Множественное наследование
# toyota = Car(brand='toyota', model='sport')
# toyota.fast_start()
