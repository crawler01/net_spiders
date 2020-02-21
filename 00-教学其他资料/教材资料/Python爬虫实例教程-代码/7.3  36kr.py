import requests
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'}

pre_url = 'http://36kr.com/api/search-column/mainsite?per_page=20&page='
urls = [pre_url + str(x) for x in range(1,11)]
for url in urls:
    r = requests.get(url, headers = headers)
    response = r.json()
    for item in response['data']['items']:
        title = item['title']
        id  = item['id']
        #构造文章url
        item_url = 'http://36kr.com/p/' + id + '.html'