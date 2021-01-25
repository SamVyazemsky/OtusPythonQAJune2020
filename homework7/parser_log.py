import re
from collections import Counter
import json


def test_check_log(path_to_file):
    with open(path_to_file, "r") as log:
        try:
            info = log.readlines(), "\n"
            for row in info:
                get = re.findall('GET', str(row))
                post = re.findall('POST', str(row))
                times = re.findall('(.*?) "-"', str(row))
                sb = []
                for i in times:
                    if i == "":
                        continue
                ba = sorted(sb, reverse=True)
                break
        except OSError:
            print('Не возможно обработать файл!')

    with open("..//homework7//analysts.json", "w") as json_log:
        try:
            sum_request = [json.dumps(len(row), indent=4)]
            sum_get = [json.dumps(len(get), indent=4)]
            sum_post = [json.dumps(len(post), indent=4)]
            long_t = [json.dumps(ba[0:10], indent=4)]
            for request, get, post, l in zip(sum_request, sum_get, sum_post, long_t):
                json_log.write(f'Общее количество выполненных запросов - {request}' + '\n')
                json_log.write(f'Количество запросов по типу: GET - {get}' + '\n')
                json_log.write(f'Количество запросов по типу: POST -  {post}' + '\n')
                json_log.write(f'топ 10 запросов, которые завершились ошибкой со стороны сервера:' + '\n')
                for ip, count in Counter(row).most_common(10):
                    json_log.write(f'IP адрес - {ip} , сделаны запросов - {count}' + '\n')
        except OSError:
            print('Не открывается файл!')
