import random 
from tictactoe.domain.players.player import Player 
from tictactoe.domain.constants import ROBOT_TYPE 
from tictactoe.domain.constants import X, MAX_ROBOT_WINS
from tictactoe.common.position_verifier import assume_one_or_more_open_positions


class RobotPlayer(Player):
    
    @assume_one_or_more_open_positions
    def place_marker_on(self, board) -> int:
        """
        Uses a simple, naive strategy: placing a marker at random among the 
        available positions. This is a 0-move lookahead strategy. That is, it 
        doesn't consider its opponent's move after its next move. 

        Parameters
        ----------
        board : GameBoard
            The current state of the game's board representation.

        Returns
        -------
        int
            An admissible position among the empty spaces on the board.
        """
        choice = random.choice(board.empty_spaces())
        print(f"Robot with marker {self.current_marker().symbol} selected position: {choice}")
        return choice
    
    def choose_next_marker(self) -> None:
        if self.current_marker() != X:
            self.set_marker(self.opposite_marker())
        print(f"\nRobot {self.current_marker()} chose {self.current_marker().symbol}")

    def prompt_to_continue(self) -> bool:
        return self.win_count < MAX_ROBOT_WINS

    def player_type(self) -> str:
        return ROBOT_TYPE    
        
    
if __name__ == "__main__": 
    print("Working inside RobotPlayer")