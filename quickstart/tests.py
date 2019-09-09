from django.test import TestCase


from tornado.httpclient import HTTPClient
import time
def synchronous_fech(url):
    http_client = HTTPClient()
    response = http_client.fetch(url)
    print(response.body)
    print('http 网络不通，但是我还能跑')
    return response.body

# Create your tests here.
if __name__ == '__main__':
    synchronous_fech('https://www.baidu.com')

