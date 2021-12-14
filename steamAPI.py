# import requests

# API_key = "AF90EFF02499BB3CDDFFF28629DEA47B"
# steam_id_tom = "76561198084867313"
# steam_id_brendan = "76561198172219198"

# # response = requests.get(f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={API_key}&steamids={steam_id_brendan}").json()

# # friendresponse = requests.get(f'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={API_key}&steamid={steam_id_brendan}&relationship=friend').json()

# # print(friendresponse)

# def printFriendInfo(ids):
#     userurid = f'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={API_key}&steamid={ids}&relationship=friend'
#     userget = requests.get(userurid).json()['response']
#     for id in range(len(userget['players'])):
#         print(userget['players'][id])

# printFriendInfo(steam_id_tom)


#!/usr/local/bin/python3
#steam_snake.py
# Get a Steam API here:   https://steamcommunity.com/dev
# You can look up Steam IDs by URL here:   https://steamid.io/

# We're only going to need the 'requests' module
import requests

tehapi = 'AF90EFF02499BB3CDDFFF28629DEA47B'
tehuid = '76561198084867313' # This is to retrieve your friends list. Your profile needs to be set to public for this to work.
tehuri = 'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=' + tehapi + '&steamid=' + tehuid + '&relationship=friend'

## Get list of your Steam friends 
#+(if any profiles are private, you will not see their current status/game)
friendlist = requests.get(tehuri).json()['friendslist']['friends']

steamidlist = []
# For each friend json item, retrieve the Steam ID of each friend and append it to a list/array
for i in range(len(friendlist)):
    steamidlist.append(friendlist[i]['steamid'])

# Convert the list/array to a comma-separated list of Steam user IDs for the API to retrieve.
joinedsids = ','.join(steamidlist)

## Function I wrote to print out friend data in json format.
#+ call the function printFriendInfo() by passing a comma-separated
#+ list of SteamID64 IDs, e.g. (the following IDs are fake):
#+      printFriendInfo(09812409,234890234,0982130)
def printFriendInfo(ids):
    useruri = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=' + tehapi + '&steamids=' + ids
    userget = requests.get(useruri).json()['response']
    for i in range(len(userget['players'])):
        print(userget['players'][i])

# This function gets 
def printOnlineFriends(ids):
    useruri = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=' + tehapi + '&steamids=' + ids
    userget = requests.get(useruri).json()['response']

    onlineDict = {}
    global maxnamelen
    maxnamelen = 0
    for i in range(len(userget['players'])):
        tonli = userget['players'][i]['personastate']
        if tonli == 1:
            #They're online. Are they playing a game? Does the 'gameextrainfo' key exist?
            if 'gameextrainfo' in userget['players'][i]:
                sname = userget['players'][i]['personaname']
                sgame = userget['players'][i]['gameextrainfo']
                onlineDict.update( {sname : sgame} )
                if len(sname) > maxnamelen:
                    maxnamelen = int(len(sname))
            # onlineArray.append(userget['players'][i]['personaname'])
        else:
            # not online and not playing a game. continue to the next fren
            continue
    
    sortDict = sorted(onlineDict.items(), key=lambda z: z[1])
    for i in sorted (onlineDict.keys()):
    # for i in sorted (sortDict):
        tspaces = ""
        lennamediff = (maxnamelen - len(i)) + 2
        for x in range(lennamediff):
            tspaces += ' '
        print(i + tspaces, "[" + onlineDict[i] + "]")
        # END printOnlineFriends

printOnlineFriends(joinedsids)