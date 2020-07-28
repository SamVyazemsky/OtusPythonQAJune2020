from pytest import fixture

file = open('tests/url_data.txt', 'r')
r = file.readlines()
new_lst = [i.strip('\n') for i in r]
file.close()


@fixture(name='url_data', params=new_lst)
def get_url_data(request):
    yield request.param
    print('test234')
