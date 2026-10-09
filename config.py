__all__ = ['MIN_PLAYERS', 'MAX_PLAYERS', 'PlayerDatabase', 'PlayerCount', 'ImposterCount', 'Word', 'Hint']

# Playercount Rules (Immutable)
MIN_PLAYERS = 3 # don't go below 3 players, it's literally unplayable
MAX_PLAYERS = 15 # this *can* be change, but it's not recommended

# Modals -- Modals can be found in JSON files in modals/modals.

# Player Database (Mutable)
PlayerDatabase = {}

# Player Counts (Mutable)
PlayerCount = 0
ImposterCount = 0

# Word and Hint Storage (Mutable)
Word = ""
Hint = ""

"""
PlayerDatabase Example = {
    1: {
        "name": "bill",
        "imposter": True,
        "starts": False
    },
    2: {
        "name": "alice",
        "imposter": False,
        "starts": True
    },
    3: {
        "name": "charlie",
        "imposter": False,
        "starts": False
    }
}
"""