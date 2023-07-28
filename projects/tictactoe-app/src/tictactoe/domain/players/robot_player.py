import random 
from tictactoe.domain.players.player import Player 
from tictactoe.domain.constants import ROBOT_TYPE 
from tictactoe.domain.constants import X, MAX_ROBOT_WINS
from tictactoe.common.position_verifier import verify_marker_can_be_placed_on


class RobotPlayer(Player):
    
    def place_marker_on(self, board) -> int:
        verify_marker_can_be_placed_on(board)
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