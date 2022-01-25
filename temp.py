from urllib.request import urlopen
import json
API_key = 'AF90EFF02499BB3CDDFFF28629DEA47B'
user_ID = '76561198084867313'

userurl = 'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={API_key}&steamid={user_ID}&relationship=friend'

user = urlopen(userurl)
user_data = json.loads(user.read())
friendlist_code = []

for friend in user_data['friendslist']['friends']:
    friendlist_code.append(friend['steamid'])

for friend in friendlist_code:
    url = f'https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={API_Key}&steamid={x}'
    
print(url)
print(userurl)
print(friendlist_code)