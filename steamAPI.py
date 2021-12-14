import requests

API_key = "AF90EFF02499BB3CDDFFF28629DEA47B"
steam_id_tom = "76561198084867313"
steam_id_brendan = "76561198172219198"

response = requests.get(f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={API_key}&steamids={steam_id_brendan}").json()

friendresponse = requests.get(f' http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={API_key}&steamid={steam_id_brendan}&relationship=friend').json()

print(friendresponse)