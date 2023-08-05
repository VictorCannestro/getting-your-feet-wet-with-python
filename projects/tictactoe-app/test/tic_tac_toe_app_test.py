import pytest
from src.tictactoe.tic_tac_toe_app import TicTacToeApp
from src.tictactoe.domain.players.human_player import HumanPlayer
from src.tictactoe.domain.players.robot_player import RobotPlayer 
from src.tictactoe.domain.players.advanced_robot_player import AdvancedRobotPlayer 
from src.tictactoe.domain.constants import X, O
from src.tictactoe.infrastructure.views.text_based_user_interface import TextBasedUserInterface 


class LaunchIntegrationTest(object):
    
    text_ui = TextBasedUserInterface()
    
    
    def test_happy_path_scenario_x_wins(self, monkeypatch):
        first_player, second_player = HumanPlayer(X, self.text_ui), HumanPlayer(O, self.text_ui)
        app = TicTacToeApp(first_player, second_player, self.text_ui)
        responses = iter(['0', '6', '1', '7', '2', 'n'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        app.launch()  
        assert first_player.get_win_count() == 1
        assert second_player.get_win_count() == 0

    def test_happy_path_scenario_o_wins(self, monkeypatch):
        first_player, second_player = HumanPlayer(X, self.text_ui), HumanPlayer(O, self.text_ui)
        app = TicTacToeApp(first_player, second_player, self.text_ui)
        responses = iter(['0', '6', '1', '7', '4', '8', 'n'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        app.launch()  
        assert first_player.get_win_count() == 0
        assert second_player.get_win_count() == 1
        
    def test_happy_path_scenario_draw(self, monkeypatch):
        first_player, second_player = HumanPlayer(O, self.text_ui), HumanPlayer(X, self.text_ui)
        app = TicTacToeApp(first_player, second_player, self.text_ui)
        responses = iter(['0', '3', '6', '2', '5', '8', '1', '4', '7', 'n'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        app.launch()  
        assert first_player.get_win_count() == 0
        assert second_player.get_win_count() == 0

    def test_happy_path_scenario_x_wins_twice(self, monkeypatch):
        first_player, second_player = HumanPlayer(X, self.text_ui), HumanPlayer(O, self.text_ui)
        app = TicTacToeApp(first_player, second_player, self.text_ui)
        responses = iter(['0', '6', '1', '7', '2', 'y', 'y', 'X', '0', '6', '1', '7', '2', 'n'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        app.launch()  
        assert first_player.get_win_count() == 2
        assert second_player.get_win_count() == 0
        
    def test_conflicting_robot_player_markers(self, monkeypatch):
        first_player, second_player = RobotPlayer(X), AdvancedRobotPlayer(X)
        with pytest.raises(ValueError) as exception_info: 
            TicTacToeApp(first_player, second_player, self.text_ui)
        assert exception_info       

    
if __name__ == "__main__": 
    pass