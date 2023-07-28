from collections import namedtuple


ADMISSABLE_POSITIONS = range(9)

HUMAN_TYPE = "Human Player"
ROBOT_TYPE = "Robot"
MAX_ROBOT_WINS = 2

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

VictoryThreshold = namedtuple("VictoryThreshold", ["value"])
ENOUGH_TO_WIN = VictoryThreshold(3)
  
    
if __name__ == "__main__": 
    print("Constants file has been accessed")