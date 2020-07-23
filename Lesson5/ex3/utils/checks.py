import json


class CheckStatusCode:
    def isSuccess(self, response):
        assert response.status_code == 200
        return

    def isAccepted(self, response):
        assert response.status_code == 202
        return

    def isNoContent(self, response):
        assert response.status_code == 204
        return

    def isRedirect(self, response):
        assert response.status_code == 302
        return

    def isClientError(self, response):
        assert response.status_code == 400
        return

    def isServerError(self, response):
        assert response.status_code == 500
        return


class CheckHeaders:

    def checkHeaderIn(self, header, response):
        key, value = header.popitem()
        responseJson = json.loads(response.text)
        assert key in responseJson['headers']
        assert value == responseJson['headers'][key]
        return            


