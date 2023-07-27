from tictactoe.domain.players.Player import Player 
from tictactoe.domain.gameboard import GameBoard 
from tictactoe.domain.Constants import X, O, AVAILABLE_MARKERS
from tictactoe.domain.Constants import YES, AVAILABLE_DECISIONS 
from tictactoe.common.MarkerVerifier import pick_from
from tictactoe.common.ChoiceVerifier import decide_from
from tictactoe.common.PositionVerifier import select_position_from, verify_marker_can_be_placed_on



class HumanPlayer(Player):
        
    def place_marker_on(self, board: GameBoard) -> int:
        verify_marker_can_be_placed_on(board)
        return select_position_from(board)
    
    def choose_next_marker(self) -> None:
        self.set_marker(X if pick_from(AVAILABLE_MARKERS) == X.symbol else O)    
    
    def prompt_to_continue(self) -> bool:
        return True if decide_from(AVAILABLE_DECISIONS) == YES.symbol else False
    
   

if __name__ == "__main__": 
    player = HumanPlayer(X)
    print(player.current_marker())