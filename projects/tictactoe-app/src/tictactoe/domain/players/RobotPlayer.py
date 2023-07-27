import random 
from tictactoe.domain.players.Player import Player 
from tictactoe.domain.Constants import X
from tictactoe.common.PositionVerifier import verify_marker_can_be_placed_on



class RobotPlayer(Player):
        
    def place_marker_on(self, board) -> int:
        verify_marker_can_be_placed_on(board)
        choice = random.choice(board.empty_spaces())
        print(f"Robot selected position: {choice}")
        return choice
    
    def choose_next_marker(self) -> None:
        if self.current_marker() != X:
            self.set_marker(self.opposite_marker())
        print(f"\nRobot is {self.current_marker().symbol}")
        
        
        
if __name__ == "__main__": 
    robot = RobotPlayer(X)
    print(robot.current_marker())