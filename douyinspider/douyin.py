import requests
from douyinspider.utils import downloadCategory, downloadBillboard

if __name__ == '__main__':
    downloadCategory()
    # response = requests.get(URL.billboard(), headers=common_headers).json()
    # print(response)
