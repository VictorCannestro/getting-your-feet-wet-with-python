import pytest
from src.tictactoe.domain.constants import Marker, X, O, AVAILABLE_MARKERS
from src.tictactoe.common.marker_verifier import verify_is_available, verify_markers_do_not_conflict, pick_from



class VerifyIsAvailableTest(object):
    def test_X_is_available(self):
        assert verify_is_available(X) == True
        
    def test_O_is_available(self):
        assert verify_is_available(O) == True
        
    def test_nonXO_marker_not_available(self):
        D = Marker("D")
        with pytest.raises(ValueError) as exception_info: 
            verify_is_available(D)
        assert exception_info 
        

class VerifyMarkersDoNotConflictTest(object):
    def test_XO_constants_do_not_conflict(self):
        assert verify_markers_do_not_conflict(X,O) == True
        
    def test_OX_constants_do_not_conflict(self):
        assert verify_markers_do_not_conflict(O,X) == True

    def test_conflicting_markers_should_raise_error(self):
        D, E = Marker("D"), Marker("D")
        with pytest.raises(ValueError) as exception_info: 
            verify_markers_do_not_conflict(D,E)
        assert exception_info 
        

class PickFromTest(object):
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
        user_input = pick_from(AVAILABLE_MARKERS)
        assert user_input == X.symbol

    def test_pick_from_o_matches_valid_marker_object(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: O.symbol)
        user_input = pick_from(AVAILABLE_MARKERS)
        assert user_input == O.symbol

    @pytest.mark.parametrize("test_data", test_yes_data, ids=test_x_ids)
    def test_pick_from_with_initial_bad_input_conitnues_prompting_until_x(self, monkeypatch, test_data):
        responses = iter(test_data)
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        user_input = pick_from(AVAILABLE_MARKERS)
        assert user_input == X.symbol

    @pytest.mark.parametrize("test_data", test_no_data, ids=test_o_ids)
    def test_pick_from_with_initial_bad_input_conitnues_prompting_until_o(self, monkeypatch, test_data):
        responses = iter(test_data)
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        user_input = pick_from(AVAILABLE_MARKERS)
        assert user_input == O.symbol        
        
    def test_pick_from_without_match_continues_to_prompt_until_input_exhausted(self, monkeypatch):
        responses = iter(['asd', '12df', ' ', '-123', 'H', '`', '['])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        with pytest.raises(StopIteration) as exception_info: 
            pick_from(AVAILABLE_MARKERS)
        assert exception_info 



if __name__ == "__main__": 
    pass
