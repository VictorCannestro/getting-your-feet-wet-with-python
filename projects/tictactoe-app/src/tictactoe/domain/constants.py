from collections import namedtuple


Dimensions = namedtuple("Dimensions", ["rows", "columns"])
DIM = Dimensions(3, 3)
ADMISSIBLE_POSITIONS = range(DIM.rows * DIM.columns)

BoardType = namedtuple("BoardType", ["is_current_board_type"])
WIDE = BoardType(DIM.rows < DIM.columns)
SQUARE = BoardType(DIM.rows == DIM.columns)
TALL = BoardType(DIM.rows > DIM.columns)

Decision = namedtuple("Decision", ["symbol"])
YES = Decision("y")
NO = Decision("n")
AVAILABLE_DECISIONS = (YES.symbol, NO.symbol)

Marker = namedtuple("Marker", ["symbol"])
X = Marker("X")
O = Marker("O")
EMPTY = Marker("-")
AVAILABLE_MARKERS = (X.symbol, O.symbol)

Outcome = namedtuple("Outcome", ["is_game_over", "winner"])
X_WON = Outcome(True, X)
O_WON = Outcome(True, O)
DRAW = Outcome(True, None)
GAME_NOT_FINISHED = Outcome(False, None) 
  
HUMAN_TYPE = "Human"
ROBOT_TYPE = "Robot"
MAX_ROBOT_WINS = 2
