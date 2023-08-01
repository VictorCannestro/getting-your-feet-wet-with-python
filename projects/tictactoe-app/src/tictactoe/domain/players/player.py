from abc import ABC, abstractmethod
from tictactoe.domain.gameboard.game_board import GameBoard 
from tictactoe.domain.constants import Marker, X, O
from tictactoe.common.marker_verifier import verify_is_available


class Player(ABC):

    def __init__(self, marker: Marker) -> None:
        verify_is_available(marker) 
        self.marker = marker
        self.win_count = 0
        
    def current_marker(self) -> Marker:
        return self.marker
    
    def opposite_marker(self) -> Marker:
        return X if self.current_marker() == O else O
    
    def set_marker(self, marker: Marker) -> None:
        verify_is_available(marker) 
        self.marker = marker    
    
    def is_x_player(self) -> bool:
        return True if self.current_marker() == X else False
    
    def tally_a_win(self) -> None:
        self.win_count += 1
    
    def get_win_count(self) -> int:
        return self.win_count
       
    @abstractmethod
    def place_marker_on(self, board: GameBoard) -> int:
       pass    
     
    @abstractmethod
    def choose_next_marker(self) -> None:
       pass  

    @abstractmethod
    def prompt_to_continue(self) -> bool:
        pass

    @abstractmethod
    def player_type(self) -> str:
        pass
   
    
if __name__ == "__main__": 
    pass