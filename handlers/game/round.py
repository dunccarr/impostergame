import random
def startround(playerdatabase):
    print()
    print()
    for playerid in playerdatabase:
        player = playerdatabase[playerid]
        if player["starts"]:
            print(f"{player['name']} starts the round. The game will be played in a {random.choice(['clockwise', 'counter-clockwise'])} rotation.")
            break