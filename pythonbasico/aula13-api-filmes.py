import requests

apiKey = None

try:
    apiKey = open("apiKey.txt").read()
except Exception as err:
    print("Couldn't read the file. Error:", err)
    exit()

req = None

try:
    req = requests.get(f"https://www.omdbapi.com/?t=Interstellar&apikey={apiKey}")
except Exception as err:
    print("Connection error:", err)
    exit()

print(req.text)
