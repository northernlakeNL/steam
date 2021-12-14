import requests

API_key = "AF90EFF02499BB3CDDFFF28629DEA47B"
steam_id = "76561198084867313"

response = requests.get(f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={API_key}&steamids={steam_id}").json()

print(response)