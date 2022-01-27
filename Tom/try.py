import requests
genre = requests.get('https://github.com/northernlakeNL/steam/blob/8be8ba89da587fff1691829c76b5a8fc8961d032/Tom/popular_genres.txt')
if genre.status_code == requests.codes.ok:
    req = genre.json()
print(req)