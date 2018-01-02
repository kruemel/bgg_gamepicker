from picker_app import db
from picker_app import Game
from boardgamegeek import BGGClient

def get_games():

    # Constants
    GOOD_THRESH = 0.2
    BAD_THRESH = 0.2
    MIN_VOTES = 20
    USERNAME = "Truphy"

    bgg = BGGClient()
    print("Getting collection from BGG..")
    collection = bgg.collection(USERNAME, exclude_subtype='boardgameexpansion', own=True, wishlist=None)
    ids = [x.id for x in collection.items]
    game_list = []

    # get games from BGG
    try:
        print("Getting games from BGG..")
        game_list = bgg.game_list(ids)
        if not game_list:
            print("Error: empy list returned.")
    except:
        print("An Error occured..")
        raise TimeoutError
    else:
        print("Done.")
    return game_list, collection
