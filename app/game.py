from enum import Enum
from typing import Tuple
from collections import namedtuple

from app.map import Map, Sign, Cell
from app.player import Player, Person, Computer


class State(Enum):
    ACTIVE = "active"
    DRAW = "Draw"
    VICTORY = "Victory"

class Game:
    def __init__(self, map: Map, players: namedtuple):
        self.map = map
        self.players = players
        self.current_player = self._define_order()
        self.state = self._get_state()

    def _define_order(self) -> Player:
        #order in self.players: (person, computer)
        if self.map.counter[Cell(Sign.CROSS)] == self.map.counter[Cell(Sign.TAUGHT)]:
            sign_order = (Sign.CROSS, Sign.TAUGHT)
        else:
            sign_order = (Sign.TAUGHT, Sign.CROSS)
        for player, sign in zip(self.players, sign_order):
            player.set_sign(sign)
            player.create_move_gen()
        else:
            return self.players.person          

    def _get_state(self) -> State:
        if self._check_victory():
            return State.VICTORY
        if self._check_draw():
            return State.DRAW
        return State.ACTIVE

    def _check_victory(self):
        check_directions = [
            [[(row, col) for row in range(0, 3)] for col in range(0, 3)],
            [[(row, col) for col in range(0, 3)] for row in range(0, 3)],
            [[(0, 0), (1, 1), (2, 2)], [(2, 0), (1, 1), (0, 2)]]
        ]
        #sign: Sign = self._change_player().sign
        for direction in check_directions:
            for line in direction:
                for sign in {Cell(Sign.CROSS), Cell(Sign.TAUGHT)}:
                    if all([self.map[i][j] == sign for i, j in line]):
                        return State.VICTORY
        return False
    
    def _check_draw(self):
        for row in self.map:
            if any(
                [Sign.EMPTY == cell.value for cell in row]):
                return False
        return True

    def _change_player(self):
        if self.current_player == self.players.person:
            return self.players.computer
        return self.players.person
    
    def start(self):      
        print(self.map)
        
        if self.state == State.ACTIVE:
            next(self.current_player.move)
            self.state = self._get_state()    

        while True:
            print(self.map)
            match self.state:
                case State.ACTIVE:
                    self.current_player = self._change_player()
                    next(self.current_player.move)  
                    self.state = self._get_state()   
                case State.DRAW:
                    print("DRAW!")
                    break
                case State.VICTORY:
                    print(f"{self.current_player.name} WITH {self.current_player.sign.value}-sign WINS!")
                    break 