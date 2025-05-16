import requests

api_key ="2e959e91cdcf4f028120bc99cdd0b7a7"
url =("https://newsapi.org/v2/everything?"\
      "q=tesla&from=2025-04-16&sortBy=publishedAt&apiKey="\
      "2e959e91cdcf4f028120bc99cdd0b7a7")

request = requests.get(url)
content = request.json()
for article in content["articles"]:
      print(article["title"])
      print(article["description"])
