from abc import ABC, abstractmethod
from tictactoe.domain.gameboard.game_board import GameBoard


class UserInteractable(ABC):   
    
    @abstractmethod  
    def pick_from(available_markers: tuple) -> str:
        pass       
   
    @abstractmethod  
    def decide_from(available_decisions: tuple) -> str:
        pass   
   
    @abstractmethod  
    def select_position_from(self, board: GameBoard) -> int:
        pass   
    
   
if __name__ == "__main__": 
    pass