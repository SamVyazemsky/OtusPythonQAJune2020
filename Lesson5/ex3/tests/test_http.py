import pytest
import json
from utils.checks import CheckStatusCode, CheckHeaders
#import ApiClient

checkHeaders = CheckHeaders()
checkStatusCode = CheckStatusCode()

apiClient = ApiClient(host='httpbin.org')


@pytest.mark.parametrize('header', [{'Testheader': 'some value'}], ids=['Testheader:someValue'])
def test_headers(header):
    response = apiClient.getHeaders(headers=header)

    checkStatusCode.isSuccess(response=response)

    checkHeaders.checkHeaderIn(header=header, response=response)


@pytest.mark.parametrize('code, method, check', [
    (200, apiClient.getStatus, checkStatusCode.isSuccess),
    (202, apiClient.putStatus, checkStatusCode.isAccepted),
    (204, apiClient.postStatus, checkStatusCode.isNoContent),
    (400, apiClient.patchStatus, checkStatusCode.isClientError),
    (500, apiClient.deleteStatus, checkStatusCode.isServerError)
], ids=['200 get',
        '202 put',
        '204 post',
        '400 patch',
        '500 delete'])
def test_statusCode(code, method, check):
    response = method(code)

    check(response)


@pytest.mark.parametrize('redirectTimes, allowRedirects, check', [
    (2, False, checkStatusCode.isRedirect),
    (3, True, checkStatusCode.isSuccess)
], ids=['Redirect allowed',
        'Redirect not allowed'])
def test_redirects(basic_auth, redirectTimes, allowRedirects, check):
    response = apiClient.getRedirects(redirectTimes=redirectTimes, allowRedirects=allowRedirects)
    check(response)
