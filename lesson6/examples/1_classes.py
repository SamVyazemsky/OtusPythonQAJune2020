class Animal:
    pass


class Car:
    color = 'white'


# Создание экземпляра класса
cat = Animal()
dog = Animal()

toyota = Car()
honda = Car()

print('dog is example of class Animal', isinstance(dog, str))
print('cat is example of class Animal', isinstance(cat, Animal))
print('honda is example of class Car', isinstance(honda, Car))
print('toyota is example of class Car', isinstance(dog, Car))

hamster = Animal
print('hamster is example of class Animal', isinstance(hamster, Animal))
# new = hamster()
# print('new is example of class Animal', isinstance(new, Animal))
