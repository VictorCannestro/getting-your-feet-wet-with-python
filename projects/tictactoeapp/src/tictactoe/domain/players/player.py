from abc import ABC, abstractmethod
from tictactoe.domain.gameboard.game_board import GameBoard 
from tictactoe.domain.constants import Marker, X, O


class Player(ABC):

    def __init__(self, marker: Marker) -> None:
        self.marker = marker
        
    def current_marker(self) -> Marker:
        return self.marker
    
    def opposite_marker(self) -> Marker:
        return X if self.marker == O else O
    
    def set_marker(self, marker: Marker) -> None:
        self.marker = marker    
       
    @abstractmethod
    def place_marker_on(self, board: GameBoard) -> int:
       pass    
     
    @abstractmethod
    def choose_next_marker(self) -> None:
       pass  
       
   
    
if __name__ == "__main__": 
    pass