from tictactoe.domain.gameboard.game_board import GameBoard
from tictactoe.domain.players.human_player import HumanPlayer 
from tictactoe.domain.players.robot_player import RobotPlayer 
from tictactoe.domain.constants import Marker, X, O, AVAILABLE_MARKERS 
from tictactoe.domain.constants import Decision
from tictactoe.common.marker_verifier import pick_from, verify_markers_do_not_conflict



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
                    game_over, winner = self._human_players_turn(X, self.board)
                    if game_over:
                        break
                    game_over, winner = self._robot_players_turn(O, self.board)
                    if game_over:
                        break
                else:
                    game_over, winner = self._robot_players_turn(X, self.board)
                    if game_over:
                        break
                    game_over, winner = self._human_players_turn(O, self.board)
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
    
    def _human_players_turn(self, marker: Marker, board) -> Decision:
        board.display()
        board.register(marker, self.human_player.place_marker_on(board))
        return board.determine_if_game_has_ended()    

    def _robot_players_turn(self, marker: Marker, board) -> Decision:
        board.register(marker, self.robot_player.place_marker_on(board))
        return board.determine_if_game_has_ended()                
    
    def _declare_game_results(self, winner: Marker) -> None:
        self.board.display()
        if not winner:
            print("The game ended in a draw." )
        else:
            print(f"The game has ended. {winner.symbol} has won.")
    
    def _setup_new_game(self, winner: Marker) -> None:
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