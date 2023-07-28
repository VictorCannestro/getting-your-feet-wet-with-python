from tictactoe.domain.exceptions import CannotMakeMove
from tictactoe.domain.constants import ADMISSABLE_POSITIONS


ADMISSABLE_STR_POSITIONS = tuple(str(n) for n in ADMISSABLE_POSITIONS)


def verify_is_admissible(position: int) -> bool:        
    if position not in ADMISSABLE_POSITIONS:
        raise ValueError("position must be an integer from 0 to 9.")     
    return True         

def verify_marker_can_be_placed_on(board) -> bool: 
    if not board.empty_spaces():
        raise CannotMakeMove("An impossible state has been reached: A player has been prompted for a move, but there are no more playable moves.")
    return True                     

def select_position_from(board) -> int:
    player_input = input("Position of your next move: ")
    while not(player_input in ADMISSABLE_STR_POSITIONS and _position_is_available(player_input, board)):
        print("Not an available position. Choose again.")
        player_input = input("Position of your next move: ")
    return int(player_input)

def _position_is_available(position: str, board) -> bool:
    return int(position) in board.empty_spaces()


if __name__ == "__main__": 
    print("Working inside PositionVerifier")