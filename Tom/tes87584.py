# def searchboi(value, lst):
#     low = 0
#     high = len(lst) -1
#     mid = 0
#     while low <= high:
#         mid = (low + high) // 2
#         if value <= lst[mid]:
#             high = mid
#         else:
#             low = mid
#         if low == high:
#             return True
#         elif low+1 == high:
#             return lst[high] == value or lst[low] == value




# def find(L, target):
#     start = 0
#     end = len(L) - 1
#     L.sort()
#     print(L)
#     while start <= end:
#         middle = (start + end) // 2
#         midpoint = L[middle]
#         if midpoint > target:
#             end = middle - 1
#         elif midpoint < target:
#             start = middle + 1
#         else:
#             return midpoint

# L = ["Brian", "Joe", "Lois", "Meg", "Peter", "Stewie"] # Needs to be sorted.

# lijst =  ['invoering', 'actueel', 'gefinancierd', 'seksisme', 'hoger', 'afwerken', 'contract', 'entameren', 'bestudering', 'groeve']
# value = 'seksisme'


import time
from urllib.request import urlopen
import json
URL = 'https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=AF90EFF02499BB3CDDFFF28629DEA47B&steamids=76561198084867313'
json_file = urlopen(URL)
data = json.loads(json_file.read())

for x in data['response']['players']:
    seconds = x['timecreated']
date = time.gmtime(seconds)
year = date[0]
month = date[1]
day = date[2]
print(day, month, year)