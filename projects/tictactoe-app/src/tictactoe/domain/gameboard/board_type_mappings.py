from tictactoe.domain.constants import Dimensions, BoardType, WIDE, SQUARE, TALL


def current_global_boardtype():
    if SQUARE.is_current_board_type:
        return SQUARE
    return TALL if TALL.is_current_board_type else WIDE

def determine_boardtype_from(dimensions: Dimensions) -> BoardType:
    return determine_boardtype(dimensions.rows, dimensions.columns)

def determine_boardtype(rows: int, columns: int) -> BoardType:
    if rows == columns:
        return SQUARE
    return TALL if rows > columns else WIDE