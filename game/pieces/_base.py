from dataclasses import dataclass
from enum import Enum

class Color(Enum):
  white = 1
  black = 2

board = [[[] for i in range(57)] for i in range(57)]

@dataclass
class Piece:
  color: Color

  def move(self, board, x, y):
    pass

  def legals(self, board):
    pass

  def around(self, x):
    if x % 2:
      return [(0,-1), (+1,0), (+1,+1), (0,+1), (-1,+1), (-1,0)]
    else:
      return [(0,-1), (+1,-1), (+1,0), (0,+1), (-1,0), (-1,-1)]

  def can_move_on_ground(self, board, x, y):
    for idx, (i,j) in enumerate(self.around(x)):
      if board[x+i][y+j][0]:
          next_i, next_j = self.around(x)[idx + 1]
          if board[x+next_i][y+next_j][0]:
              return True
    return False