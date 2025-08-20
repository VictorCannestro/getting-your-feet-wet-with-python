from tictactoe.domain.constants import Marker, X, O, Dimensions
from tictactoe.domain.constants import Outcome
from tictactoe.domain.gameboard.game_board import GameBoard
from tictactoe.domain.players.player import Player
from tictactoe.common.marker_verifier import verify_markers_do_not_conflict
from tictactoe.domain.players.robot import Robot
from tictactoe.ports.outbound.displayable import Displayable
from tictactoe.infrastructure.views.text_based_user_interface import TextBasedUserInterface


class TicTacToeApp:
    
    def __init__(
            self,
            user_interface: Displayable,
            first_player: Player = Robot(X),
            second_player: Player = Robot(O),
            dimensions: Dimensions = Dimensions(3, 3)
    ) -> None:
        self.user_interface = user_interface
        self.first_player = first_player
        self.second_player = second_player
        verify_markers_do_not_conflict(first_player.current_marker(), second_player.current_marker())
        self.board = GameBoard(dimensions)
        self.continue_playing = True
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
                self._setup_new_game_based_on(winner)

    def _player_turn_action(self, marker: Marker, player: Player) -> Outcome:
        self.user_interface.display_current(self.board) 
        self.board.register(marker, player.place_marker_on(self.board))
        return self.board.determine_if_game_has_ended()                   
    
    def _declare_game_results(self, winner: Marker) -> None:
        self.user_interface.display_current(self.board) 
        if not winner:
            self.user_interface.display_draw_message()
        else:
            self.user_interface.display_win_message(winner)
            if self.first_player.current_marker() == winner: 
                self.first_player.tally_a_win()  
            else:
                self.second_player.tally_a_win()
    
    def _setup_new_game_based_on(self, winner: Marker) -> None:
        self.board.reset()
        if self.first_player.current_marker() == winner:
            self.first_player.choose_next_marker()
            self.second_player.set_marker(self.first_player.opposite_marker())
        else:
            self.second_player.choose_next_marker()
            self.first_player.set_marker(self.second_player.opposite_marker())
        print(f"Player 1 ({self.first_player.player_type()}) is {self.first_player.current_symbol()}")
        print(f"Player 2 ({self.second_player.player_type()}) is {self.second_player.current_symbol()}")
    
    
if __name__ == "__main__":
    from tictactoe.domain.players.human import Human
    from tictactoe.domain.players.minimax_robot import MinimaxRobot

    text_ui = TextBasedUserInterface()
    p1 = Human(X, text_ui)
    p2 = MinimaxRobot(p1.opposite_marker())
    app = TicTacToeApp(text_ui, p1, p2)
    app.launch()