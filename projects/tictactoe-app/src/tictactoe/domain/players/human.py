from tictactoe.domain.players.player import Player 
from tictactoe.domain.gameboard.game_board import GameBoard
from tictactoe.domain.constants import HUMAN_TYPE 
from tictactoe.domain.constants import Marker, X, O, AVAILABLE_MARKERS
from tictactoe.domain.constants import YES, AVAILABLE_DECISIONS 
from tictactoe.ports.inbound.user_interactable import UserInteractable
from tictactoe.common.position_verifier import assume_one_or_more_open_positions


class Human(Player):
    
    def __init__(self, marker: Marker, user_interaction: UserInteractable) -> None:
        super().__init__(marker)
        self.user_interaction = user_interaction
    
    @assume_one_or_more_open_positions
    def place_marker_on(self, board: GameBoard) -> int:
        return self.user_interaction.select_position_on(board)
    
    def choose_next_marker(self) -> None:
        self.set_marker(X if self.user_interaction.pick_from(AVAILABLE_MARKERS) == X.symbol else O)    
    
    def prompt_to_continue(self) -> bool:
        return self.user_interaction.decide_from(AVAILABLE_DECISIONS) == YES.symbol
    
    def player_type(self) -> str:
        return HUMAN_TYPE 
    
    
if __name__ == "__main__": 
    pass