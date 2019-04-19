from urllib.parse import urlparse, parse_qs
import urllib

url = "http://101.251.217.210/rest/n/feed/hot?app=0&lon=121.372027&c=BOYA_BAIDU_PINZHUAN&sys=ANDROID_4.1.2&mod=HUAWEI(HUAWEI%20C8813Q)&did=ANDROID_e0e0ef947bbbc243&ver=5.4&net=WIFI&country_code=cn&iuid=&appver=5.4.7.5559&max_memory=128&oc=BOYA_BAIDU_PINZHUAN&ftt=&ud=0&language=zh-cn&lat=31.319303&type=7&page=2&count=20&coldStart=false&pv=false&id=5&refreshTimes=4&pcursor=1&os=android&client_key=3c2cd3f3&sig=22769f2f5c0045381203fc57d1b5ad9b"

result = urlparse(url)
query = result.query
query_dict = query.split('&')
params_dict = {}
for query_str in query_dict:
    query_params = query_str.split('=')
    k = query_params[0]
    v = query_params[1]
    if k == 'sig' or k == '__NStokensig':
        continue
    params_dict[k] = urllib.parse.unquote(v)
params = sorted(params_dict.keys())


new_params = []
for k in params:
    new_params.append(k+'='+params_dict[k])

new_params_url = ''.join(new_params)
import hashlib
m2 = hashlib.md5()
m2.update(new_params_url.encode('utf-8'))

print(m2.hexdigest())
