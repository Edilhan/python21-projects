import requests

url = 'https://wikiway.com/upload/iblock/edd/Oslo.jpg'
res = requests.get(url)
# print(res.content)
name = 'photos/photo1.jpg'

with open(name, "wb") as file:
    file.write(res.content)