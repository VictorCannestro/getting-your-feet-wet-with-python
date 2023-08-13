from tictactoe.domain.players.player import Player 
from tictactoe.domain.gameboard.game_board import GameBoard
from tictactoe.domain.constants import HUMAN_TYPE 
from tictactoe.domain.constants import Marker, X, O, AVAILABLE_MARKERS
from tictactoe.domain.constants import YES, AVAILABLE_DECISIONS 
from tictactoe.adapters.inbound.user_interactable import UserInteractable 
from tictactoe.common.position_verifier import assume_one_or_more_open_positions


class HumanPlayer(Player):
    
    def __init__(self, marker: Marker, player_interaction: UserInteractable):
        super().__init__(marker)
        self.player_interaction = player_interaction
    
    @assume_one_or_more_open_positions
    def place_marker_on(self, board: GameBoard) -> int:
        return self.player_interaction.select_position_from(board)
    
    def choose_next_marker(self) -> None:
        self.set_marker(X if self.player_interaction.pick_from(AVAILABLE_MARKERS) == X.symbol else O)    
    
    def prompt_to_continue(self) -> bool:
        return True if self.player_interaction.decide_from(AVAILABLE_DECISIONS) == YES.symbol else False
    
    def player_type(self) -> str:
        return HUMAN_TYPE 
    
    
if __name__ == "__main__": 
    pass