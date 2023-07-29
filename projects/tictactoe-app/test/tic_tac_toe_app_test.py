import pytest
from src.tictactoe.tic_tac_toe_app import TicTacToeApp
from src.tictactoe.domain.players.human_player import HumanPlayer 
from src.tictactoe.domain.constants import X, O


class LaunchIntegrationTest(object):
    
    def test_happy_path_scenario_x_wins(self, monkeypatch):
        first_player, second_player = HumanPlayer(X), HumanPlayer(O)
        app = TicTacToeApp(first_player, second_player)
        responses = iter(['0', '6', '1', '7', '2', 'n'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        app.launch()  
        assert first_player.get_win_count() == 1
        assert second_player.get_win_count() == 0

    def test_happy_path_scenario_o_wins(self, monkeypatch):
        first_player, second_player = HumanPlayer(X), HumanPlayer(O)
        app = TicTacToeApp(first_player, second_player)
        responses = iter(['0', '6', '1', '7', '4', '8', 'n'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        app.launch()  
        assert first_player.get_win_count() == 0
        assert second_player.get_win_count() == 1
        
    def test_happy_path_scenario_draw(self, monkeypatch):
        first_player, second_player = HumanPlayer(O), HumanPlayer(X)
        app = TicTacToeApp(first_player, second_player)
        responses = iter(['0', '3', '6', '2', '5', '8', '1', '4', '7', 'n'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        app.launch()  
        assert first_player.get_win_count() == 0
        assert second_player.get_win_count() == 0

    def test_happy_path_scenario_x_wins_twice(self, monkeypatch):
        first_player, second_player = HumanPlayer(X), HumanPlayer(O)
        app = TicTacToeApp(first_player, second_player)
        responses = iter(['0', '6', '1', '7', '2', 'y', 'y', 'X', '0', '6', '1', '7', '2', 'n'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        app.launch()  
        assert first_player.get_win_count() == 2
        assert second_player.get_win_count() == 0
        
    def test_conflicting_human_player_markers(self, monkeypatch):
        first_player, second_player = HumanPlayer(X), HumanPlayer(X)
        with pytest.raises(ValueError) as exception_info: 
            TicTacToeApp(first_player, second_player)
        assert exception_info       

    
if __name__ == "__main__": 
    pass