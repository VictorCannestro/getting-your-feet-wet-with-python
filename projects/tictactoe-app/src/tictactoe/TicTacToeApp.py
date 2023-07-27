from tictactoe.domain.gameboard.GameBoard import GameBoard 
from tictactoe.domain.players.HumanPlayer import HumanPlayer 
from tictactoe.domain.players.RobotPlayer import RobotPlayer 
from tictactoe.domain.Constants import Marker, X, O, AVAILABLE_MARKERS 
from tictactoe.common.MarkerVerifier import pick_from, verify_markers_do_not_conflict



class TicTacToeApp():
    
    __LOGO = """
▀█▀ █ █▀▀ ▀█▀ ▄▀█ █▀▀ ▀█▀ █▀█ █▀▀
░█░ █ █▄▄ ░█░ █▀█ █▄▄ ░█░ █▄█ ██▄
"""
    
    
    def __init__(self) -> None:
        self._display_the_rules()
        self.board = GameBoard()
        self.board.display_demo_board()
        self.human_player = HumanPlayer(self._players_initial_choice())
        self.robot_player = RobotPlayer(self.human_player.opposite_marker())
        self.continue_playing = True
        
    def launch(self) -> None:
        while self.continue_playing:
            winner = None
            game_over = False
            while not game_over:
                if self.human_player.current_marker() == X:
                    self.board.display()
                    self.board.register(X, self.human_player.place_marker_on(self.board))
                    game_over, winner = self.board.determine_if_game_has_ended()
                    if game_over:
                        break
                    self.board.register(O, self.robot_player.place_marker_on(self.board))
                    game_over, winner = self.board.determine_if_game_has_ended()
                    if game_over:
                        break
                else:
                    self.board.register(X, self.robot_player.place_marker_on(self.board))
                    game_over, winner = self.board.determine_if_game_has_ended()
                    if game_over:
                        break
                    self.board.display()
                    self.board.register(O, self.human_player.place_marker_on(self.board))
                    game_over, winner = self.board.determine_if_game_has_ended()
                    if game_over:
                        break
            self._declare_game_results(winner)
            self.continue_playing = self.human_player.prompt_to_continue()
            if self.continue_playing:
                self._setup_new_game(winner)
        print("Thank you for playing.")
        
    def _display_the_rules(self) -> None:
        print(self.__LOGO)
        print("How to win: get three markers in a row, column, or diagonal.")
        print("X goes first.")
    
    def _players_initial_choice(self) -> Marker:
        verify_markers_do_not_conflict(X, O)
        return X if pick_from(AVAILABLE_MARKERS) == X.symbol else O
    
    def _declare_game_results(self, winner) -> None:
        self.board.display()
        if not winner:
            print("The game ended in a draw." )
        else:
            print(f"The game has ended. {winner.symbol} has won.")
    
    def _setup_new_game(self, winner) -> None:
        self.board.reset()
        if self.human_player.current_marker() == winner:
            self.human_player.choose_next_marker()
            self.robot_player.set_marker(self.human_player.opposite_marker())
        elif self.robot_player.current_marker() == winner:
            self.robot_player.choose_next_marker()
            self.human_player.set_marker(self.robot_player.opposite_marker())
        else:
            print("After a draw both players will keep their current markers.")
        print(f"Player is {self.human_player.current_marker().symbol}")
    

    
if __name__ == "__main__":
    app = TicTacToeApp()
    app.launch()