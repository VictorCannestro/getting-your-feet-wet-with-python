import pytest
from src.tictactoe.domain.constants import ADMISSABLE_POSITIONS
from src.tictactoe.domain.constants import X, O
from tictactoe.domain.exceptions import CannotMakeMove
from src.tictactoe.domain.gameboard.game_board import GameBoard
from src.tictactoe.common.position_verifier import verify_is_admissible, verify_marker_can_be_placed_on, select_position_from



class VerifyIsAdmissibleTest(object):
    
    positions = tuple(ADMISSABLE_POSITIONS)
    non_admissible_positions = (-1, "3", 9, 10, 1.3, "y", "X", " ", "")
        
    @pytest.mark.parametrize("position", positions)
    def test_with_admissible_input(self, position):
        assert verify_is_admissible(position)

    @pytest.mark.parametrize("position", non_admissible_positions)
    def test_with_non_admissible_input(self, position):
        with pytest.raises(ValueError) as exception_info: 
            verify_is_admissible(position)
        assert exception_info 


class VerifyMarkerCanBePlacedOnTest(object):
    
    draw_game_positions = ((X, 0), (X, 1), (O, 2), 
                            (O, 3), (O, 4), (X, 5), 
                            (X, 6), (X, 7), (O, 8)) 
    

    def test_verify_marker_can_be_placed_on_empty_board(self):
        empty_board = GameBoard()
        assert verify_marker_can_be_placed_on(empty_board)  == True

    def test_verify_marker_can_be_placed_on_board_with_open_spaces(self):
        test_board = GameBoard()
        marker_position_pairs = ((X, 0), (X, 1), (O, 2), 
                                 (O, 3), (O, 4), (X, 5), 
                                 (X, 6), (X, 7)) 
        for marker, position in marker_position_pairs:
            test_board.register(marker, position)
            assert verify_marker_can_be_placed_on(test_board) == True
        
    def test_verify_marker_cannot_be_placed_on_full_board(self):
        draw_board = GameBoard()
        for marker, position in self.draw_game_positions:
            draw_board.register(marker, position)
        with pytest.raises(CannotMakeMove) as exception_info: 
            verify_marker_can_be_placed_on(draw_board)
        assert exception_info                
        
        
class SelectPositionFromTest(object):

    test_invalid_then_admissible_data = [
            (X.symbol, "0"), ("YES", "1"), ("Y", "2"), (" ", "3"), ("", "4"),
            (1.03, "5"), (True, "6"), (-1, "7"), ("\n", "8"), ("9", "0")
        ]
    
    test_ids = [
            "test_alphabetic_char_as_input",
            "test_multiple_characters_as_input",
            "test_capitol_character_as_input",
            "test_space_as_input",
            "test_empty_as_input",
            "test_float_as_input",
            "test_bool_as_input",
            "test_right_boundary_condition_as_input",
            "test_slash_n_as_input",
            "test_left_boundary_condition_as_input"
        ]
    
    
    def test_select_admissible_position_from_empty_board(self, monkeypatch):
        empty_board = GameBoard()
        monkeypatch.setattr('builtins.input', lambda _: "0")
        user_input = select_position_from(empty_board)
        assert user_input == 0

    def test_select_occupied_position_from_board(self, monkeypatch):
        board = GameBoard()
        board.register(X, 0)
        responses = iter(['0', '1'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        assert select_position_from(board) == 1

    @pytest.mark.parametrize("test_data", test_invalid_then_admissible_data, ids=test_ids)
    def test_invalid_position_from_empty_board_conitnues_prompting_until_valid(self, monkeypatch, test_data):
        empty_board = GameBoard()
        invalid_input, valid_input = test_data
        responses = iter(test_data)
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        assert select_position_from(empty_board) == int(valid_input)     
        
    def test_select_position_from_without_match_continues_to_prompt_until_input_exhausted(self, monkeypatch):
        empty_board = GameBoard()
        responses = iter(['asd', '12df', ' ', '-123', 'H', '`', '['])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        with pytest.raises(StopIteration) as exception_info: 
            select_position_from(empty_board)
        assert exception_info 



if __name__ == "__main__": 
    pass