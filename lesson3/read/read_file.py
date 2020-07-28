file = open('../data/data.txt', 'rb')

# чтение всего файла
print(file.read())

# количество символов
# print(file.read(20))

# построчно
# print(file.readline())
# print(file.readline())
# print(file.read())

# список
# print(file.readlines())

# построчно
# for item in file:
#     print(item)

file.close()
