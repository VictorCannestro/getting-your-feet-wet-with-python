from abc import ABC, abstractmethod
from tictactoe.domain.gameboard.game_board import GameBoard


class UserInterface(ABC):

    @abstractmethod
    def display_logo(self) -> None:
        pass   
    
    @abstractmethod
    def display_demo_board(self) -> None:
        pass
    
    @abstractmethod   
    def display_current(self, board: GameBoard) -> None:
        pass

    @abstractmethod  
    def display_the_rules(self) -> None:
       pass
       
   
if __name__ == "__main__": 
    pass