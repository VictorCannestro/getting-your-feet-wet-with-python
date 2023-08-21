from tictactoe.domain.exceptions import CannotMakeMove
from tictactoe.domain.constants import ADMISSIBLE_POSITIONS
from functools import wraps


def assume_position_is_admissible(func):
    @wraps(func)
    def wrapper_func(class_reference, marker, position):
        verify_is_admissible(position)
        return func(class_reference, marker, position)
    return wrapper_func

def assume_one_or_more_open_positions(func):
    @wraps(func)
    def wrapper_func(class_reference, board):
        verify_marker_can_be_placed_on(board)
        return func(class_reference, board)
    return wrapper_func

def verify_is_admissible(position: int) -> bool:        
    if position not in ADMISSIBLE_POSITIONS:
        raise ValueError(f"Position must be an integer from 0 to 9. Received: {position}")
    return True         

def verify_marker_can_be_placed_on(board) -> bool: 
    if not board.empty_spaces():
        raise CannotMakeMove("An impossible state has been reached: A player has been prompted for a move, but there are no more playable moves.")
    return True                     

def admissible_str_positions() -> tuple:
    return tuple(str(n) for n in ADMISSIBLE_POSITIONS)
