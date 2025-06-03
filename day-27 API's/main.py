import requests
from send_email import send_email

# this the Api key from news Api
api_key = "2e959e91cdcf4f028120bc99cdd0b7a7"

url = ("https://newsapi.org/v2/everything?"\
      "q=tesla&from=2025-04-16&sortBy=publishedAt&apiKey="\
      "2e959e91cdcf4f028120bc99cdd0b7a7&language=en")

# this requesting for url
request = requests.get(url)

# this line making data as dictionary
content = request.json()
body = ""
# this is for looping the Api articles
for article in content["articles"][:20]:
    if article["title"] is not None:
        description = article["description"] if article["description"] is not None else "No description"
        body = ("subject: Today's news"+body + article["title"] + "\n" + description + "\n" + \
                article["url"] + 2 * "\n")

body = body.encode("utf-8")
send_email(message=body)
