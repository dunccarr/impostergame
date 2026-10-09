def getplayercount(min_players: int, max_players: int):
    print()
    print("How many players are there?")
    players = 0
    while True:
        try:
            players = int(input("> "))
        except ValueError:
            continue
        
        if min_players <= players <= max_players:
            return players