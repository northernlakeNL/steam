lst = [
   {
      "appid":10,
      "name":"Counter-Strike",
      "release_date":"2000-11-01",
      "english":1,
      "developer":"Valve",
      "publisher":"Valve",
      "platforms":"windows;mac;linux",
      "required_age":0,
      "categories":"Multi-player;Online Multi-Player;Local Multi-Player;Valve Anti-Cheat enabled",
      "genres":"Action",
      "steamspy_tags":"Action;FPS;Multiplayer",
      "achievements":0,
      "positive_ratings":124534,
      "negative_ratings":3339,
      "average_playtime":17612,
      "median_playtime":317,
      "owners":"10000000-20000000",
      "price":7.19
   },
   {
      "appid":20,
      "name":"Team Fortress Classic",
      "release_date":"1999-04-01",
      "english":1,
      "developer":"Valve",
      "publisher":"Valve",
      "platforms":"windows;mac;linux",
      "required_age":0,
      "categories":"Multi-player;Online Multi-Player;Local Multi-Player;Valve Anti-Cheat enabled",
      "genres":"Action",
      "steamspy_tags":"Action;FPS;Multiplayer",
      "achievements":0,
      "positive_ratings":3318,
      "negative_ratings":633,
      "average_playtime":277,
      "median_playtime":62,
      "owners":"5000000-10000000",
      "price":3.99
   },
   {
      "appid":30,
      "name":"Day of Defeat",
      "release_date":"2003-05-01",
      "english":1,
      "developer":"Valve",
      "publisher":"Valve",
      "platforms":"windows;mac;linux",
      "required_age":0,
      "categories":"Multi-player;Valve Anti-Cheat enabled",
      "genres":"Action",
      "steamspy_tags":"FPS;World War II;Multiplayer",
      "achievements":0,
      "positive_ratings":3416,
      "negative_ratings":398,
      "average_playtime":187,
      "median_playtime":34,
      "owners":"5000000-10000000",
      "price":3.99
   }
]





for x in lst:
    print(x["appid"])