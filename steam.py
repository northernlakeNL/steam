import requests

API_key = "XXXXXXXXXXXXXXXXX"

response = requests.get("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=XXXXXXXXXXXXXXXXXXXXX&steamids=XXXXXXX").json()

print(response)
