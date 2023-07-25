from typing import Tuple
from itertools import chain
from collections import namedtuple

from app.game import Game
from app.map import Map
from app.player import Person, Computer

# todo: 
#   Occupied cell and messages
#   TypeHints
#   ComputerLogic
#   Readability
#   Pytest
#   Exceptions

        
if __name__ == "__main__":
    initial_state = "_________"
    map = Map(initial_state)
    Participants = namedtuple("Participants", ["person", "computer"])
    players = Participants(Person(map), Computer(map))
    game = Game(
        map=map,
        players=players
    )
    try:
        game.start()
    except ValueError as e:
        print(e)

