import requests

url = "https://download.samplelib.com/mp3/sample-3s.mp3"
response = requests.get(url)

content = response.content

with open("download.mp3", "wb") as f:
    f.write(content)
