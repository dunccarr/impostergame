def endgame(playerdatabase, word):
    print()
    input("Once the round is complete, press enter...\t")
    print()
    print()
    imposter = []
    for playerid in playerdatabase:
        if playerdatabase[playerid]["imposter"]:
            imposter.append(playerdatabase[playerid]["name"])
    print(f"The imposter(s): {imposter}")
    print(f"The word: '{word}'")
    
    print()
    print()
    
    print("Thanks for playing ImposterGame!")