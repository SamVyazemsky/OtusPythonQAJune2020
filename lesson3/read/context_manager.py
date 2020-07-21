# with open('../data/data.txt', 'r') as file:
#     item = file.read()
#
# print(item)

with open('../data/data.txt', 'r') as file:
    for item in file.readlines():
        print(item)
