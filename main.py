from modals.modal import Modal
from pathlib import Path
import config
import json


def main():
    # main menu
    main_menu_path = Path(__file__).parent / "modals" / "modals" / "mainmenu.json"
    main_menu = Modal(main_menu_path)

    match main_menu.render():
        case 1:
            # start new game
            pass

        case 2:
            # show instructions
            from handlers.mainmenu.instructions import instructions
            instructions()

            # main menu with no instructions
            main_menu2_path = Path(__file__).parent / "modals" / "modals" / "mainmenu2.json"
            main_menu_2 = Modal(main_menu2_path)

            match main_menu_2.render():
                case 1:
                    # start new game
                    pass

                case 2:
                    # quit
                    from handlers.mainmenu.endscript import endscript
                    endscript()

        case 3:
            from handlers.mainmenu.endscript import endscript
            endscript()

    # game setup

    # get player count input
    from handlers.player.playercount import getplayercount
    player_count = getplayercount(config.MIN_PLAYERS, config.MAX_PLAYERS)
    config.PlayerCount = player_count

    # get players input
    from handlers.player.players import getplayers
    players = getplayers(config.PlayerCount)

    # add players to the player database
    for playerid, player in enumerate(players, start=1):
        config.PlayerDatabase[playerid] = {
            "name": player,
            "imposter": False,
            "starts": False
        }

    # get imposter count
    from handlers.imposter.impostercount import getimpostercount
    imposters = getimpostercount(config.PlayerCount)
    config.ImposterCount = imposters

    # get imposters
    from handlers.imposter.imposters import getimposters
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
    from handlers.game.round import startround
    startround(config.PlayerDatabase)

    # end the game
    from handlers.game.endgame import endgame
    endgame(config.PlayerDatabase, config.Word)


if __name__ == "__main__":
    main()