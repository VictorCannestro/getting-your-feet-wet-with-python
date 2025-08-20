import pytest
from tictactoe.tic_tac_toe_app import TicTacToeApp
from tictactoe.domain.players.human import Human
from tictactoe.domain.players.robot import Robot
from tictactoe.domain.players.minimax_robot import MinimaxRobot
from tictactoe.domain.constants import X, O, Dimensions
from tictactoe.infrastructure.views.text_based_user_interface import TextBasedUserInterface


class LaunchIntegrationTest(object):
    
    text_ui = TextBasedUserInterface()
    
    
    def test_happy_path_scenario_x_wins(self, monkeypatch):
        dim, p1, p2 = Dimensions(3, 3), Human(X, self.text_ui), Human(O, self.text_ui)
        app = TicTacToeApp(self.text_ui, p1, p2, dim)
        responses = iter(['0', '6', '1', '7', '2', 'n'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        app.launch()  
        assert p1.get_win_count() == 1
        assert p2.get_win_count() == 0

    def test_happy_path_scenario_o_wins(self, monkeypatch):
        dim, p1, p2 = Dimensions(3, 3), Human(X, self.text_ui), Human(O, self.text_ui)
        app = TicTacToeApp(self.text_ui, p1, p2, dim)
        responses = iter(['0', '6', '1', '7', '4', '8', 'n'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        app.launch()  
        assert p1.get_win_count() == 0
        assert p2.get_win_count() == 1
        
    def test_happy_path_scenario_draw(self, monkeypatch):
        dim, p1, p2 = Dimensions(3, 3), Human(O, self.text_ui), Human(X, self.text_ui)
        app = TicTacToeApp(self.text_ui, p1, p2, dim)
        responses = iter(['0', '3', '6', '2', '5', '8', '1', '4', '7', 'n'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        app.launch()  
        assert p1.get_win_count() == 0
        assert p2.get_win_count() == 0

    def test_happy_path_scenario_x_wins_twice(self, monkeypatch):
        dim, p1, p2 = Dimensions(3, 3), Human(X, self.text_ui), Human(O, self.text_ui)
        app = TicTacToeApp(self.text_ui, p1, p2, dim)
        responses = iter(['0', '6', '1', '7', '2', 'y', 'y', 'X', '0', '6', '1', '7', '2', 'n'])
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        app.launch()  
        assert p1.get_win_count() == 2
        assert p2.get_win_count() == 0
        
    def test_conflicting_robot_player_markers(self, monkeypatch):
        dim, p1, p2 = Dimensions(3, 3), Robot(X), MinimaxRobot(X)
        with pytest.raises(ValueError) as exception_info: 
            TicTacToeApp(self.text_ui, p1, p2, dim)
        assert exception_info       

    
if __name__ == "__main__": 
    pass