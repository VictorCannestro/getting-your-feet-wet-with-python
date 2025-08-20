import pytest
from tictactoe.domain.constants import Dimensions
from tictactoe.domain.constants import X, O
from tictactoe.domain.gameboard.game_board import GameBoard
from tictactoe.domain.exceptions import PositionOccupied
from tictactoe.domain.constants import X_WON, O_WON, DRAW, GAME_NOT_FINISHED


def make_3x3_board():
    return GameBoard(Dimensions(3, 3))

def fill_3x3_board(positions) -> GameBoard:
    board = make_3x3_board()
    for marker, position in positions:
        board.register(marker, position)
    return board


class GameBoardTest(object):
    
    draw_game_positions = ((X, 0), (X, 1), (O, 2), 
                           (O, 3), (O, 4), (X, 5), 
                           (X, 6), (X, 7), (O, 8))   
  

    x_won_game_positions = ((X, 0), (O, 1), (O, 2), 
                            (X, 3), (O, 4), (X, 5), 
                            (X, 6)) 
    
    o_won_game_positions = ((X, 0), (X, 1), (O, 2), 
                            (X, 3), (O, 4), 
                            (O, 6)) 
        
    unfinished_game_positions = ((X, 0), (O, 1), (X, 2), 
                                 (X, 3), (O, 4), (X, 5), 
                                 (O, 6)) 
            
    @pytest.mark.parametrize("position", make_3x3_board().admissible_positions())
    def test_verify_marker_cannot_be_placed_on_full_board(self, position: int):
        draw_board = fill_3x3_board(self.draw_game_positions)
        with pytest.raises(Exception) as exception_info: 
            draw_board.register(O, position) 
        assert exception_info.typename == PositionOccupied.__name__

    def test_draw_outcome(self):
        draw_board = fill_3x3_board(self.draw_game_positions)
        assert draw_board.determine_if_game_has_ended() == DRAW
        
    def test_x_won_outcome(self):
        board = fill_3x3_board(self.x_won_game_positions)
        assert board.determine_if_game_has_ended() == X_WON        
        
    def test_o_won_outcome(self):
        draw_board = fill_3x3_board(self.o_won_game_positions)
        assert draw_board.determine_if_game_has_ended() == O_WON
        
    def test_game_not_finished_outcome(self):
        board = fill_3x3_board(self.unfinished_game_positions)
        assert board.determine_if_game_has_ended() == GAME_NOT_FINISHED
        
    def test_board_reset(self):
        board = make_3x3_board()
        board.register(X, 0)
        board.reset()
        assert len(board.empty_spaces()) == len(board.admissible_positions())


if __name__ == "__main__": 
    pass