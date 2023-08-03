import pytest
from src.tictactoe.domain.gameboard.game_board import GameBoard
from src.tictactoe.infrastructure.views.text_based_user_interface import TextBasedUserInterface 
from src.tictactoe.domain.constants import Decision, YES, NO, AVAILABLE_DECISIONS
from src.tictactoe.domain.constants import Marker, X, O, AVAILABLE_MARKERS



class DecideFromTest(object):
    
    text_ui = TextBasedUserInterface()   
    
    test_yes_data = [("1", YES.symbol), ("YES", YES.symbol), ("Y", YES.symbol), (" ", YES.symbol), ("", YES.symbol)]
    test_no_data = [(1.03, NO.symbol), (True, NO.symbol), (-1, NO.symbol), ("\n", NO.symbol), (Decision("W").symbol, NO.symbol)]
    
    test_yes_ids = ["test_number_as_input",
                "test_multiple_characters_as_input",
                "test_capitol_character_as_input",
                "test_space_as_input",
                "test_empty_as_input"]
    
    test_no_ids = ["test_float_as_input",
                "test_bool_as_input",
                "test_negative_int_as_input",
                "test_slash_n_as_input",
                "test_nonvalid_decision_as_input"]
    
    
    def test_decide_from_y_matches_valid_decision_object(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: YES.symbol)
        assert self.text_ui.decide_from(AVAILABLE_DECISIONS) == YES.symbol

    def test_decide_from_n_matches_valid_decision_object(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: NO.symbol)
        assert self.text_ui.decide_from(AVAILABLE_DECISIONS) == NO.symbol

    @pytest.mark.parametrize("test_data", test_yes_data, ids=test_yes_ids)
    def test_decide_from_with_initial_bad_input_conitnues_prompting_until_yes(self, monkeypatch, test_data):
        responses = iter(test_data)
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        assert self.text_ui.decide_from(AVAILABLE_DECISIONS) == YES.symbol

    @pytest.mark.parametrize("test_data", test_no_data, ids=test_no_ids)
    def test_decide_from_with_initial_bad_input_conitnues_prompting_until_no(self, monkeypatch, test_data):
        responses = iter(test_data)
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        assert self.text_ui.decide_from(AVAILABLE_DECISIONS) == NO.symbol        
        
    def test_decide_from_without_match_continues_to_prompt_until_input_exhausted(self, monkeypatch):
        responses = iter(['asd', '12df', ' ', '-123', 'H', '`', '['])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        with pytest.raises(StopIteration) as exception_info: 
            self.text_ui.decide_from(AVAILABLE_DECISIONS)
        assert exception_info 
            

class PickFromTest(object):

    text_ui = TextBasedUserInterface()
        
    test_yes_data = [("1", X.symbol), ("YES", X.symbol), ("Y", X.symbol), (" ", X.symbol), ("", X.symbol)]
    test_no_data = [(1.03, O.symbol), (True, O.symbol), (-1, O.symbol), ("\n", O.symbol), (Marker("W").symbol, O.symbol)]
    
    test_x_ids = ["test_number_as_input",
                "test_multiple_characters_as_input",
                "test_capitol_character_as_input",
                "test_space_as_input",
                "test_empty_as_input"]
    
    test_o_ids = ["test_float_as_input",
                "test_bool_as_input",
                "test_negative_int_as_input",
                "test_slash_n_as_input",
                "test_nonvalid_decision_as_input"]
    
    
    def test_pick_from_x_matches_valid_marker_object(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: X.symbol)
        assert self.text_ui.pick_from(AVAILABLE_MARKERS) == X.symbol

    def test_pick_from_o_matches_valid_marker_object(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: O.symbol)
        assert self.text_ui.pick_from(AVAILABLE_MARKERS) == O.symbol

    @pytest.mark.parametrize("test_data", test_yes_data, ids=test_x_ids)
    def test_pick_from_with_initial_bad_input_conitnues_prompting_until_x(self, monkeypatch, test_data):
        responses = iter(test_data)
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        assert self.text_ui.pick_from(AVAILABLE_MARKERS) == X.symbol

    @pytest.mark.parametrize("test_data", test_no_data, ids=test_o_ids)
    def test_pick_from_with_initial_bad_input_conitnues_prompting_until_o(self, monkeypatch, test_data):
        responses = iter(test_data)
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        assert self.text_ui.pick_from(AVAILABLE_MARKERS) == O.symbol        
        
    def test_pick_from_without_match_continues_to_prompt_until_input_exhausted(self, monkeypatch):
        responses = iter(['asd', '12df', ' ', '-123', 'H', '`', '['])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        with pytest.raises(StopIteration) as exception_info: 
            self.text_ui.pick_from(AVAILABLE_MARKERS)
        assert exception_info 


class SelectPositionFromTest(object):
    
    text_ui = TextBasedUserInterface()
    
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
        user_input = self.text_ui.select_position_from(empty_board)
        assert user_input == 0

    def test_select_occupied_position_from_board(self, monkeypatch):
        board = GameBoard()
        board.register(X, 0)
        responses = iter(['0', '1'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        assert self.text_ui.select_position_from(board) == 1

    @pytest.mark.parametrize("test_data", test_invalid_then_admissible_data, ids=test_ids)
    def test_invalid_position_from_empty_board_conitnues_prompting_until_valid(self, monkeypatch, test_data):
        empty_board = GameBoard()
        invalid_input, valid_input = test_data
        responses = iter(test_data)
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        assert self.text_ui.select_position_from(empty_board) == int(valid_input)     
        
    def test_select_position_from_without_match_continues_to_prompt_until_input_exhausted(self, monkeypatch):
        empty_board = GameBoard()
        responses = iter(['asd', '12df', ' ', '-123', 'H', '`', '['])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        with pytest.raises(StopIteration) as exception_info: 
            self.text_ui.select_position_from(empty_board)
        assert exception_info 
        

if __name__ == "__main__": 
    pass