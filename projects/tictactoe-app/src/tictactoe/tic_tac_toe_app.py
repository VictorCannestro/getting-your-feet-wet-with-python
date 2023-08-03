from tictactoe.domain.constants import Marker, X, O 
from tictactoe.domain.constants import Decision
from tictactoe.domain.gameboard.game_board import GameBoard
from tictactoe.domain.players.player import Player
from tictactoe.common.marker_verifier import verify_markers_do_not_conflict
from tictactoe.adapters.outbound.displayable import Displayable


class TicTacToeApp():   
    
    def __init__(self, first_player: Player, second_player: Player, user_interface: Displayable) -> None:
        self.board = GameBoard()
        self.continue_playing = True
        self.first_player = first_player
        self.second_player = second_player
        self.user_interface = user_interface
        verify_markers_do_not_conflict(first_player.current_marker(), second_player.current_marker())
        self.user_interface.display_logo()
        self.user_interface.display_the_rules()
        self.user_interface.display_demo_board()        
        
    def launch(self) -> None:
        while self.continue_playing:
            winner = None
            game_over = False
            while not game_over:
                if self.first_player.is_x_player(): 
                    game_over, winner = self._player_turn_action(X, self.first_player)
                    if game_over:
                        break
                    game_over, winner = self._player_turn_action(O, self.second_player)    
                    if game_over:
                        break
                else:
                    game_over, winner = self._player_turn_action(X, self.second_player)                    
                    if game_over:                                                
                        break
                    game_over, winner = self._player_turn_action(O, self.first_player)                    
                    if game_over:                        
                        break
            self._declare_game_results(winner)
            self.continue_playing = self.first_player.prompt_to_continue() and self.second_player.prompt_to_continue()
            if self.continue_playing:
                self._setup_new_game(winner)
        print("Thank you for playing.")
    
    def _player_turn_action(self, marker: Marker, player: Player) -> Decision:
        self.user_interface.display_current(self.board) 
        self.board.register(marker, player.place_marker_on(self.board))
        return self.board.determine_if_game_has_ended()                   
    
    def _declare_game_results(self, winner: Marker) -> None:
        self.user_interface.display_current(self.board) 
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
    from tictactoe.domain.players.human_player import HumanPlayer 
    from tictactoe.domain.players.advanced_robot_player import AdvancedRobotPlayer 
    from tictactoe.infrastructure.views.text_based_user_interface import TextBasedUserInterface

    text_ui = TextBasedUserInterface()
    first_player = HumanPlayer(X, text_ui)
    second_player = AdvancedRobotPlayer(first_player.opposite_marker())    
    app = TicTacToeApp(first_player, second_player, text_ui)
    app.launch()