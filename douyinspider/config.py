# http
fetch_timeout = 5

common_headers = {
    'User-Agent': 'Aweme 3.1.0 rv:31006 (iPhone; iOS 12.0; zh_CN) Cronet'
}

# 个人post的是是视频使用，使用上的无法拉到数据
person_post_headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

# retrying
retry_max_number = 10
retry_min_random_wait = 1000  # ms
retry_max_random_wait = 5000  # ms
