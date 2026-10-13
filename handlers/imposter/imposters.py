import random

def getimposters(playercount: int, impostercount: int):
    imposters = random.sample(range(1, playercount + 1), impostercount)
    return imposters