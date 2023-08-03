from tictactoe.domain.exceptions import CannotMakeMove
from tictactoe.domain.constants import ADMISSABLE_POSITIONS


def verify_is_admissible(position: int) -> bool:        
    if position not in ADMISSABLE_POSITIONS:
        raise ValueError("position must be an integer from 0 to 9.")     
    return True         

def verify_marker_can_be_placed_on(board) -> bool: 
    if not board.empty_spaces():
        raise CannotMakeMove("An impossible state has been reached: A player has been prompted for a move, but there are no more playable moves.")
    return True                     

def admissible_str_positions() -> tuple:
    return tuple(str(n) for n in ADMISSABLE_POSITIONS)


if __name__ == "__main__": 
    print("Working inside PositionVerifier")