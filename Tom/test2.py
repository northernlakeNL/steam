from urllib.request import urlopen
import requests

url = 'https://github.com/northernlakeNL/'

# steam/blob/d2ee42d4cf6acda5b6ca9eec186698503e888cf6/Tom/popular_genres.txt

r = requests.get(url, auth=('northernlakeNL', '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'))

print(r.status_code)
print(r.headers)