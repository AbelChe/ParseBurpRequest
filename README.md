# ParseBurpRequest
python 解析burp请求包 将请求包解析为python对象 方便requests等模块发起请求

## 使用方法

```python
from ParseBurpRequest import ParseBurpRequest # 引入类

p = ParseBurpRequest('blastmultipart.txt') # 传入请求包, 一般可以通过burp直接复制保存, 类似sqlmap -r

# 解析为如下几种数据, header cookie 请求方法 url参数 host 路径 Content-Type body数据
print('headers          ', p.headers) # header dict类型
print('cookie           ', p.getCookies()) # cookie dict类型
print('request_method   ', p.request_method) # 请求方法 str类型
print('params           ', p.params) # url参数 dict类型 
print('host             ', p.host) # host str类型
print('path             ', p.path) # 路径 str类型
print('content_type     ', p.content_type) # Content-Type str类型
print('data             ', p.data) # body数据 根据Content-Type解析为不同类型, html、xml、text等为str类型, www-form为dict类型, multipart为MultipartEncoder类型
print('jsondata         ', p.jsondata) # body数据 同上, 如果Content-Type为json格式, 那么数据会解析到jsondata 而不是data, 此举是为了方便requests
```

使用requests需要注意：
1. url需要拼接，并且需要手动添加scheme为http或者https，具体可以参考test.py
2. 如果请求为multipart/form-data类型, body数据会解析为MultipartEncoder类型`from requests_toolbelt.multipart.encoder import MultipartEncoder`, 可以直接对接requests使用，具体可以参考test.py
3. requests可以提供最简单的重放请求方式, 例如post请求, 无需考虑body数据类型, 只需提供data、json参数即可`requests.post(url=url, params=p.params, data=p.data, json=p.jsondata, headers=p.headers, verify=False)`

效果如下：
!()[1.png]
!()[2.png]
