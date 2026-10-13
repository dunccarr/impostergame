def getimpostercount(playercount: int):
    impostercount = 1

    if playercount <= 5:
        impostermax = 1
    
    elif playercount <= 8:
        impostermax = 2
        
    else:
        impostermax = 3

    if impostermax > 1:
        print()
        print(f"How many imposters do you want to play with? (1-{impostermax})")
        
        impostercount = 0
        while impostercount == 0:
            try:
                inputtovalidate = int(input("> "))
            except ValueError:
                continue
            
            if 1 <= inputtovalidate <= impostermax:
                impostercount = inputtovalidate

    return impostercount