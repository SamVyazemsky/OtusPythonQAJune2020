class Car:
    wheels = 4


    def drive(self):
        print('car is driving')

    def stop(self):
        print('car stopped')

    pass


class Animal:
    legs = 4

    def make_sound(self):
        print('Iam animal')

    def start_sleep(self):
        print('zzzzzz')


# static
toyota = Car()
# toyota.drive()
# toyota.stop()
# print(f'wheels count is {toyota.wheels}')
#
cat = Animal()
cat.make_sound()
cat.start_sleep()
print('cat have '+ str(cat.legs) +'legs')
print(f'cat have {cat.legs}')
