from collections import Counter
from typing import Tuple

from app.map import Map, Sign, Cell


class Player:
    def __init__(self, map) -> None:
        self.map = map
        self.move = None
        self.sign: Sign = None
        self.name = None

    def set_sign(self, value: Sign):
        self.sign = value

    def move_gen(self):
        pass

    def create_move_gen(self):
        self.move = self.move_gen()


class Person(Player):
    def __init__(self, map) -> None:
        super().__init__(map)
        self.name = "PERSON"

    def move_gen(self) -> tuple:
        while True:
            i, j = self._validate_input(input())
            self.map[i][j] = self.sign
            yield

    def _validate_input(self, input_coords: str) -> tuple:
        input_coords = input_coords.split()
        try:
            i, j = int(input_coords[0]) - 1, int(input_coords[-1]) - 1
        except ValueError as e:
            print("You should enter numbers!")
        if not {i, j} < {0, 1, 2}:
            raise ValueError("Coordinates should be from 1 to 3!") 
        if self.map[i][j] != Cell(Sign.EMPTY):
            raise ValueError("This cell is iccupiied. Enter another one")
        return i, j
 
 
class Computer(Player):
    def __init__(self, map) -> None:
        super().__init__(map)
        self.name = "COMPUTER"

    def move_gen(self):
        for row in self.map:
            for cell in row:
                if cell.value == Sign.EMPTY:
                    cell.value = self.sign     
                    yield