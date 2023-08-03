import pytest
from src.tictactoe.domain.constants import ADMISSABLE_POSITIONS
from src.tictactoe.domain.constants import X, O
from src.tictactoe.domain.exceptions import CannotMakeMove
from src.tictactoe.domain.gameboard.game_board import GameBoard
from src.tictactoe.common.position_verifier import verify_is_admissible, verify_marker_can_be_placed_on


class VerifyIsAdmissibleTest(object):
    
    positions = tuple(ADMISSABLE_POSITIONS)
    several_non_admissible_positions = (-1, "3", 9, 10, 1.3, "y", "X", " ", "")
        
    @pytest.mark.parametrize("position", positions)
    def test_with_admissible_input(self, position):
        assert verify_is_admissible(position)

    @pytest.mark.parametrize("position", several_non_admissible_positions)
    def test_with_non_admissible_input(self, position):
        with pytest.raises(ValueError) as exception_info: 
            verify_is_admissible(position)
        assert exception_info 


class VerifyMarkerCanBePlacedOnTest(object):
    
    draw_game_positions = [(X, 0), (X, 1), (O, 2), 
                            (O, 3), (O, 4), (X, 5), 
                            (X, 6), (X, 7), (O, 8)] 
    

    def test_verify_marker_can_be_placed_on_empty_board(self):
        empty_board = GameBoard()
        assert verify_marker_can_be_placed_on(empty_board)  == True

    def test_verify_marker_can_be_placed_on_board_with_open_spaces(self):
        test_board = GameBoard()
        positions = [(X, 0), (X, 1), (O, 2), 
                     (O, 3), (O, 4), (X, 5), 
                     (X, 6), (X, 7)]
        for marker, position in positions:
            test_board.register(marker, position)
            assert verify_marker_can_be_placed_on(test_board) == True
        
    def test_verify_marker_cannot_be_placed_on_full_board(self):
        draw_board = GameBoard()
        for marker, position in self.draw_game_positions:
            draw_board.register(marker, position)
        with pytest.raises(CannotMakeMove) as exception_info: 
            verify_marker_can_be_placed_on(draw_board)
        assert exception_info                
        

if __name__ == "__main__": 
    pass