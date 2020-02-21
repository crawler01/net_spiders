import re

import  requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
}
text = requests.get('https://bj.5i5j.com/ershoufang/n1',headers=headers).text
print(text)
if text.find('wscckey'):
    # print(True)
    # print(re.search(r'https://.+\d+', response.text).group())
    real_url = re.search(r'https://.+\d+', text).group()
    print(requests.get(real_url,headers=headers).text)
