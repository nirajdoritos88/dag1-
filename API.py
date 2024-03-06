#reading API applications
import requests


paginaresults = requests.get("https://catfact.ninja/facts")
feitjes = paginaresults.json()

print(feitjes["data"][5]['fact'])

