from collections import Counter
from itertools import chain
from enum import Enum

class Sign(Enum):
    CROSS = "x"
    TAUGHT = "0"
    EMPTY = " "

    def sign(self):
        return self.value


class Cell:
    def __init__(self, value: Sign):
        self.value = value

    def __hash__(self) -> int:
        return hash(self.value)
    
    def __eq__(self, another) -> bool:
        return self.value == another.value
    
    def __repr__(self) -> str:
        return f"Cell:{self.value}"
        

class Row:
    def __init__(self, data: list[Cell]) -> None:
        self.data = data

    def __getitem__(self, key):
        return self.data[key]
    
    def __setitem__(self, key, value):
        self.data[key].value = value


class Map:
    data = []

    def __init__(self, initial_state):
        self._check_initial_state(initial_state)
        self.data = [
            Row([
                Cell(Sign(value)) if value != "_" else Cell(Sign(" "))
                for value in initial_state[3*i: 3*(i+1)]
            ])
            for i in range(3)
        ]
        self.counter = Counter(chain(*self.data))  

    def _check_initial_state(self, initial_state):
        if len(initial_state) != 9:
            raise ValueError("Enter a state with correct length!")
        if  initial_state.count("x") - initial_state.count("0") not in {0, 1}:
            raise ValueError("Enter a correct state!")

    def update_sign_counter(self):
        pass 

    def __repr__(self):
        result = ""
        for row in self.data:
            result_row = " ".join(["|"] + [cell.value.sign() for cell in row] + ["|"]) + "\n"
            result += result_row
        border = "---------\n"
        result = border + result + border
        return result   
    
    def __iter__(self):
        return iter(self.data)
    
    def __getitem__(self, key):
        return self.data[key]
    
    def __setitem__(self, key, value):
        return self.data[key]
    