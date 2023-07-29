import pytest
from src.tictactoe.common.choice_verifier import decide_from
from src.tictactoe.domain.constants import Decision, YES, NO, AVAILABLE_DECISIONS



class DecideFromTest(object):
    
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
        assert decide_from(AVAILABLE_DECISIONS) == YES.symbol

    def test_decide_from_n_matches_valid_decision_object(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: NO.symbol)
        assert decide_from(AVAILABLE_DECISIONS) == NO.symbol

    @pytest.mark.parametrize("test_data", test_yes_data, ids=test_yes_ids)
    def test_decide_from_with_initial_bad_input_conitnues_prompting_until_yes(self, monkeypatch, test_data):
        responses = iter(test_data)
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        assert decide_from(AVAILABLE_DECISIONS) == YES.symbol

    @pytest.mark.parametrize("test_data", test_no_data, ids=test_no_ids)
    def test_decide_from_with_initial_bad_input_conitnues_prompting_until_no(self, monkeypatch, test_data):
        responses = iter(test_data)
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        assert decide_from(AVAILABLE_DECISIONS) == NO.symbol        
        
    def test_decide_from_without_match_continues_to_prompt_until_input_exhausted(self, monkeypatch):
        responses = iter(['asd', '12df', ' ', '-123', 'H', '`', '['])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        with pytest.raises(StopIteration) as exception_info: 
            decide_from(AVAILABLE_DECISIONS)
        assert exception_info 
            
        

if __name__ == "__main__": 
    pass