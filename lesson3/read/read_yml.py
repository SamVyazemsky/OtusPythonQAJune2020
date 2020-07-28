from yaml import dump, load, safe_load, safe_dump, FullLoader, SafeLoader

# with open('../data/data.yaml') as file:
    # a = load(file.read(), Loader=FullLoader)
    # a = load(file.read(), Loader=SafeLoader)
    # a = safe_load(file)
    # print(a)


input_dct = {'user': 'test', 'password': 'test', }
with open('dump.yml', 'w') as file:
    # dump(input_dct, file)
    safe_dump(input_dct, file)


