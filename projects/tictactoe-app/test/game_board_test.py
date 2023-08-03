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
    
    
    @pytest.mark.parametrize("position", ADMISSABLE_POSITIONS)
    def test_verify_marker_cannot_be_placed_on_full_board(self, position):
        draw_board = self._draw_board()
        with pytest.raises(PositionOccupied) as exception_info: 
            draw_board.register(O, position)
        assert exception_info 

    def test_draw_outcome(self):
        draw_board = self._draw_board()
        assert draw_board.determine_if_game_has_ended() == DRAW

    def _draw_board(self) -> GameBoard:
        draw_board = GameBoard()
        for marker, position in self.draw_game_positions:
            draw_board.register(marker, position) 
        return draw_board
    
     
if __name__ == "__main__": 
    pass