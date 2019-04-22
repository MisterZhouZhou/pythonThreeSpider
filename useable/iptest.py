#coding=utf-8
import sys
import os
import re
import urllib
import requests
import subprocess
from bs4 import BeautifulSoup


def getlocation(ip):
    url = "http://ip.cn/index.php?ip=%s" % ip
    headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
    result = requests.get(url, headers=headers).text
    soup = BeautifulSoup(result, 'html.parser')
    result_ipinfo = soup.find('div', class_='well').find_all('p')
    result_ip_content='\n'
    for info in result_ipinfo:
        result_ip_content += info.text + '\n'
    return result_ip_content

def getlocation2(ip):
    url = "http://ip.tool.chinaz.com/%s" % ip
    headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
    result = requests.get(url, headers=headers).text
    soup = BeautifulSoup(result, 'html.parser')
    result_ipinfo = soup.find('p',class_='bor-b1s').find_all('span', class_='Whwtdhalf')
    result_ip_content='\n'
    for info in result_ipinfo:
        result_ip_content += info.text + '\n'
    return result_ip_content

def tracerouteIP(ip):
    p = subprocess.Popen(['traceroute', ip], stdout=subprocess.PIPE)
    while True:
        line = p.stdout.readline()
        if not line:
            break
        search_obj = re.search(r"\(*.*.*.*\)", str(line))
        if search_obj:
            try:
                search_result = search_obj.group()
                ip = search_result.split('(')[1].split(')')[0]
                # print(getlocation(ip))
                print(getlocation2(ip))
            except IndexError as e:
                print('error'+line)
        else:
            print('===', str(line))

if __name__ == '__main__':
    import subprocess
    signature = subprocess.getoutput('echo  %s' % user_id)
    tracerouteIP('https://www.baidu.com')


