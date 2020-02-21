import requests

response = requests.get("https://www.douban.com/search?q=python")
print(response.url)
response = requests.get("https://www.douban.com/search", params={"q": "python"})
print(response.url)