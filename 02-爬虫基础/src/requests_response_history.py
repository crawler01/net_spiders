import requests

response = requests.get("http://www.jd.com/", timeout=3)
print(response.history, response.url)
