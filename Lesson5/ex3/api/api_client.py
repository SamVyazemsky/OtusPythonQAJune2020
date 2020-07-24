import requests
import logging


class ApiClient:

    def __init__(self, host):
        self.host = f'https://{host}/'

    def getHeaders(self, headers={}):
        url = self.host + 'headers'
        response = requests.get(url, headers=headers)
        return response

    def getStatus(self, code):
        url = self.host + 'status/' + str(code)
        response = requests.get(url)
        return response

    def putStatus(self, code):
        url = self.host + 'status/' + str(code)
        response = requests.put(url)
        return response

    def postStatus(self, code):
        url = self.host + 'status/' + str(code)
        response = requests.post(url)
        return response

    def patchStatus(self, code):
        url = self.host + 'status/' + str(code)
        response = requests.patch(url)
        return response

    def deleteStatus(self, code):
        url = self.host + 'status/' + str(code)
        response = requests.delete(url)
        return response

    def getRedirects(self, redirectTimes=1, allowRedirects=True):
        url = self.host + 'redirect/' + str(redirectTimes)
        response = requests.get(url, allow_redirects=allowRedirects)
        return response
