from wsgiref import headers
import requests
from ParseBurpRequest import ParseBurpRequest

p = ParseBurpRequest('blastmultipart.txt')

print('headers          ', p.headers)
print('cookie           ', p.getCookies())
print('request_method   ', p.request_method)
print('params           ', p.params)
print('host             ', p.host)
print('path             ', p.path)
print('content_type     ', p.content_type)
print('data             ', p.data)

scheme = 'http'

url = f'{scheme}://{p.host}{p.path}'
print(url)

requests.post(url=url, params=p.params, data=p.data, json=p.jsondata, headers=p.headers, proxies={'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'}, verify=False)