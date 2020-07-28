class Car:

    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    engine_status = 'off'

    def start_engine(self):
        self.engine_status = 'on'
        print(f'{self.color} {self.brand} {self.model} engine car is starting')

    def run(self):
        if self.engine_status == 'off':
            self.start_engine()
            print(f'{self.color} {self.brand} {self.brand} car is running')
        else:
            print(f'{self.color} {self.brand} {self.brand} car engine is  already running')

    def off_engine(self):
        if self.engine_status == 'on':
            print(f'{self.color} {self.brand} {self.model} engine car is turn off')
        else:
            print('car engine is already turn off')


toyota = Car(brand='Toyota', model='camry', color='blue')
toyota.run()

# toyota.start_engine()
# toyota.run()
toyota.off_engine()
