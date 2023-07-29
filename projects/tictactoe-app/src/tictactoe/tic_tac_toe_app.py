from tictactoe.domain.gameboard.game_board import GameBoard
from tictactoe.domain.players.player import Player
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
    
    
    def __init__(self, first_player: Player, second_player: Player) -> None:
        self._display_the_rules()
        self.continue_playing = True
        self.first_player = first_player
        self.second_player = second_player
        verify_markers_do_not_conflict(first_player.current_marker(), second_player.current_marker())
        self.board = GameBoard()
        self.board.display_demo_board()        
        
    def launch(self) -> None:
        while self.continue_playing:
            winner = None
            game_over = False
            while not game_over:
                if self.first_player.is_x_player(): 
                    game_over, winner = self._player_turn_action(X, self.board, self.first_player)
                    if game_over:
                        break
                    game_over, winner = self._player_turn_action(O, self.board, self.second_player)    
                    if game_over:
                        break
                else:
                    game_over, winner = self._player_turn_action(X, self.board, self.second_player)                    
                    if game_over:                                                
                        break
                    game_over, winner = self._player_turn_action(O, self.board, self.first_player)                    
                    if game_over:                        
                        break
            self._declare_game_results(winner)
            self.continue_playing = self.first_player.prompt_to_continue() and self.second_player.prompt_to_continue()
            if self.continue_playing:
                self._setup_new_game(winner)
        print("Thank you for playing.")
        
    def _display_the_rules(self) -> None:
        print(self.__LOGO)
        print("How to win: get three markers in a row, column, or diagonal.")
        print("This is a two player game in which X goes first.")
    
    def _player_turn_action(self, marker: Marker, board, player: Player) -> Decision:
        board.display()
        board.register(marker, player.place_marker_on(board))
        return board.determine_if_game_has_ended()                   
    
    def _declare_game_results(self, winner: Marker) -> None:
        self.board.display()
        if not winner:
            print("The game ended in a draw." )
        else:
            print(f"The game has ended. {winner.symbol} has won.")
            if self.first_player.current_marker() == winner: 
                self.first_player.tally_a_win()  
            else:
                self.second_player.tally_a_win()
    
    def _setup_new_game(self, winner: Marker) -> None:
        self.board.reset()
        if self.first_player.current_marker() == winner:
            self.first_player.choose_next_marker()
            self.second_player.set_marker(self.first_player.opposite_marker())
        elif self.second_player.current_marker() == winner:
            self.second_player.choose_next_marker()
            self.first_player.set_marker(self.second_player.opposite_marker())
        else:
            print("After a draw both players will keep their current markers.")
        print(f"{self.first_player.player_type()} is {self.first_player.current_marker().symbol}")
        print(f"{self.second_player.player_type()} is {self.second_player.current_marker().symbol}")
    
    
if __name__ == "__main__":
    first_player = HumanPlayer(X if pick_from(AVAILABLE_MARKERS) == X.symbol else O)
    second_player = RobotPlayer(first_player.opposite_marker())    
    app = TicTacToeApp(first_player, second_player)
    app.launch()