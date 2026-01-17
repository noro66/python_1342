from abc import ABC, abstractmethod
import random


class Player(ABC):
    def __init__(self) -> None:
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]

    def make_move(self):
        move = random.choice(self.moves)
        x_pos = move[0] + self.position[0]
        y_pos = move[1] + self.position[1]
        self.position = (x_pos, y_pos)
        self.path.append(self.position)
        return self.position

    @abstractmethod
    def level_up(self):
        pass


class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    def level_up(self):
        self.moves.extend([(1, 1), (-1, 1), (1, -1), (-1, -1)])
