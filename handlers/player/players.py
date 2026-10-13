def getplayers(playercount: int):
    print()
    players = []
    for i in range(playercount):
        print(f"What is the name of player {i + 1}?")
        playername = input("> ")
        
        if playername.strip() == "":
            playername = f"Player {i + 1}"
        
        players.append(playername)

    return players