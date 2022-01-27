def time(game_library):
    most_played = []
    time_list = []
    for game in game_library["response"]["games"]:
        if game["playtime_forever"] != 0:
            time_list.append(game["playtime_forever"])
            time_list.sort()
    for x in range(len(time_list)-10, len(time_list)):      # Tijden met games samen voegen voor de lijst
        for game in game_library["response"]["games"]:
            name = game["name"]
            if time_list[x] == game["playtime_forever"]:
                if game["playtime_forever"] >= 60:
                    hours = (game["playtime_forever"] // 60)               # Minuten in uren zetten
                    minutes = round(((game["playtime_forever"] // 60) - hours) * 60) # Overige weer terug zetten in minuten
                    play_time = f'{hours}:{minutes}'
                    most_played.append(f'{game["name"]}:{hours}:{minutes}:{play_time}')
                    return most_played
                else:
                    play_time = game["playtime_forever"]
                    return name, play_time