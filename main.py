from modals.modal import Modal
from pathlib import Path
import config
import json

# main menu

main_menu_path = Path(__file__).parent / "modals" / "modals" / "mainmenu.json"
main_menu = Modal(main_menu_path)

match main_menu.render():
    case 1:
        # start new game
        
        pass
    
    case 2:
        # show instructions
        
        from handlers.mainmenu.instructions import handlers_mainmenu_instructions
        handlers_mainmenu_instructions()
        
        # main menu with no instructions
        
        main_menu_no_instructions_path = Path(__file__).parent / "modals" / "modals" / "mainmenu2.json"
        main_menu_no_instructions = Modal(main_menu_no_instructions_path)
        
        match main_menu_no_instructions.render():
             case 1:
                 # start new game
                 
                 pass
             
             case 2:
                 # quit
                 
                 from handlers.mainmenu.quit import handlers_mainmenu_quit
                 handlers_mainmenu_quit()
        
    case 3:
        from handlers.mainmenu.quit import handlers_mainmenu_quit
        handlers_mainmenu_quit()
        
# game setup

# get player count input
from handlers.game.playercount import getplayercount
player_count = getplayercount(config.MIN_PLAYERS, config.MAX_PLAYERS)
config.PlayerCount = player_count

# get players input
from handlers.game.players import getplayers
players = getplayers(config.PlayerCount)

# add players to the player database
for playerid, player in enumerate(players, start=1):
    config.PlayerDatabase[playerid] = {
        "name": player,
        "imposter": False,
        "starts": False
    }
    
# get imposter count
from handlers.game.impostercount import getimpostercount
imposters = getimpostercount(config.PlayerCount)
config.ImposterCount = imposters

# get imposters
from handlers.game.imposters import getimposters
imposterids = getimposters(config.PlayerCount, config.ImposterCount)

# add imposter tag to player database
for imposterid in imposterids:
    config.PlayerDatabase[imposterid]["imposter"] = True
    
# get starter and add starter tag to player database
from handlers.game.startswith import getstartswith
starter = getstartswith(config.PlayerCount)
config.PlayerDatabase[starter]["starts"] = True

# give each player their word
from handlers.game.possiblewords import getwords
with open(Path(__file__).parent / "utilities" / "words.json") as f:
    possiblewords = json.load(f)
    config.Word, config.Hint = getwords(possiblewords, config.PlayerDatabase, config.PlayerCount)
    
    
# round

# start the round and rotations
from handlers.game.round import startround
startround(config.PlayerDatabase)

# end the game
from handlers.game.endgame import endgame
endgame(config.PlayerDatabase, config.Word)