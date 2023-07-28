from src.tictactoe.tic_tac_toe_app import TicTacToeApp
from src.tictactoe.domain.players.human_player import HumanPlayer 
from src.tictactoe.domain.constants import X, O


class LaunchIntegrationTest(object):
    
    def test_happy_path_scenario(self, monkeypatch):
        first_player = HumanPlayer(X)
        second_player = HumanPlayer(O)
        app = TicTacToeApp(first_player, second_player)
        happy_path_test_data = ('0', '6', '1', '7', '2', 'n', 'n')     
        responses = iter(happy_path_test_data)
        monkeypatch.setattr('builtins.input', lambda msg: next(responses))
        app.launch()  
        assert first_player.get_win_count() == 1
        assert second_player.get_win_count() == 0

    
if __name__ == "__main__": 
    pass