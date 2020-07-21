from html.parser import HTMLParser

import requests

r = requests.get("https://ya.ru")


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            print("     attr:", attr)

    def handle_endtag(self, tag):
        print("End tag :", tag)

    def handle_data(self, data):
        print(data)


parser = MyHTMLParser()
parser.feed(r.text)
