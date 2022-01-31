from urllib.request import urlopen
import requests

url = 'https://raw.githubusercontent.com/northernlakeNL/steam/d2ee42d4cf6acda5b6ca9eec186698503e888cf6/Tom/popular_genres.txt'

# steam/blob/d2ee42d4cf6acda5b6ca9eec186698503e888cf6/Tom/popular_genres.txt

file = urlopen(url)

for line in file:
    decoded = line.decode("utf-8")
    print(decoded)