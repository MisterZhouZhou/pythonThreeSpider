import urllib3
# 忽略SSL认证移除警告⚠️
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from douyinspider.utils.fetch import fetch
from douyinspider.utils.downloaderUtil import downloadBillboard, downloadCategory