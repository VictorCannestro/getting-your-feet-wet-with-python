import pytest
from src.tictactoe.domain.constants import ADMISSABLE_POSITIONS
from src.tictactoe.domain.constants import X, O
from src.tictactoe.domain.gameboard.game_board import GameBoard
from src.tictactoe.domain.exceptions import PositionOccupied
from src.tictactoe.domain.constants import X_WON, O_WON, DRAW, GAME_NOT_FINISHED


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
            
    @pytest.mark.parametrize("position", ADMISSABLE_POSITIONS)
    def test_verify_marker_cannot_be_placed_on_full_board(self, position):
        draw_board = self._fill_board(self.draw_game_positions)            
        with pytest.raises(Exception) as exception_info: 
            draw_board.register(O, position) 
        assert exception_info.typename == PositionOccupied.__name__

    def test_draw_outcome(self):
        draw_board = self._fill_board(self.draw_game_positions)
        assert draw_board.determine_if_game_has_ended() == DRAW
        
    def test_x_won_outcome(self):
        board = self._fill_board(self.x_won_game_positions)
        assert board.determine_if_game_has_ended() == X_WON        
        
    def test_o_won_outcome(self):
        draw_board = self._fill_board(self.o_won_game_positions)
        assert draw_board.determine_if_game_has_ended() == O_WON
        
    def test_game_not_finished_outcome(self):
        board = self._fill_board(self.unfinished_game_positions)
        assert board.determine_if_game_has_ended() == GAME_NOT_FINISHED
        
    def test_board_reset(self):
        board = GameBoard()
        board.register(X, 0)
        board.reset()
        assert len(board.empty_spaces()) == len(ADMISSABLE_POSITIONS)

    def test_board_admissible_positions(self):
        board = GameBoard()
        assert board.admissible_positions() == ADMISSABLE_POSITIONS
        
    def _fill_board(self, positions) -> GameBoard:
        board = GameBoard()
        for marker, position in positions:
            board.register(marker, position) 
        return board
    
     
if __name__ == "__main__": 
    pass