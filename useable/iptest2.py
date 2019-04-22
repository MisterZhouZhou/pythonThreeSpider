#tracer部分
import os
import re
import urllib3
import code

def local(ip):                                    #查询地址
    content_stream = urllib3.urlopen(ip)
    content = content_stream.read()
    print(content)
    f = open(r'text.txt','a')
    f.write(content)
    f.close()

def getIPAddFromFile(fobj):                       #分离IP
    regex = re.compile(r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b', re.IGNORECASE)
    ipadds = re.findall(regex, fobj)
    ipadds = str(ipadds)
    ipadds = ipadds.encode("utf-8")
    print(ipadds)
    return ipadds

def getiplocal(obj):                              #分离最终地址
    iplocal = re.findall("result(.*)</div>",obj)
    print(iplocal)
    return iplocal



# f = open('output.txt', 'r')                       #打开输出文件
# #print f.read()                                    #输出到屏幕
# #分离IP
# f = open('output.txt')
# txt = f.read()
# ip_list = getIPAddFromFile(txt)
# print(ip_list)
# for ip_num in ip_list:
#     ip_get = "http://ip.cn/index.php?ip=" + ip_num
#     local_address = local(ip_get)
#     print(local_address)
# #最终分割
# f = open('text.txt')
# content = f.read()
# #print content.decode('utf-8').encode('GB18030')
# temmal = getiplocal(content)
# os.system('pause')


if __name__ == '__main__':
    print("Please input target:")
    target = input()
    target_1 = "tracert " + target + " >output.txt"   #构造命令
    print("please wait ... ")
    os.system(target_1)                               #调用cmd