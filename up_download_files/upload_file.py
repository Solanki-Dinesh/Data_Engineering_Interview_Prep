import requests

url = ""
file = open("myfile.txt", "rb")

response = requests.post(url, files={"upfile":file})
