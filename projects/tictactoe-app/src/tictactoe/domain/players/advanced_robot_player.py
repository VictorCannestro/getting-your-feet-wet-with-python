import copy
from functools import lru_cache
from tictactoe.domain.players.robot_player import RobotPlayer 
from tictactoe.domain.constants import Marker, X, O
from tictactoe.domain.gameboard.game_board import GameBoard


class AdvancedRobotPlayer(RobotPlayer):
    
        
    def place_marker_on(self, board: GameBoard) -> int:
        score, next_move = self._minimax(copy.deepcopy(board), 0)
        return next_move
    
    
    @lru_cache()
    def _minimax(self, board: GameBoard, depth: int) -> tuple:
        """
        Recursive minimax at level of depth for either maximizing or minimizing
        marker.
        """
        game_over, winner = board.determine_if_game_has_ended()
        if game_over:
            return self._score(winner, depth), None

        depth += 1
        scores = []
        moves = []
        alternating_marker = self.current_marker() if depth % 2 == 1 else self.opposite_marker()
        
        for possible_move in board.empty_spaces():  
            board_copy = copy.deepcopy(board)
            board_copy.register(alternating_marker, possible_move)
            possible_game = board_copy
            scores.append(self._minimax(possible_game, depth)[0])
            moves.append(possible_move)
            
        # Do the min or the max calculation
        if alternating_marker.symbol == self.current_marker().symbol:
            max_score, max_score_index = max((score, idx) for idx, score in enumerate(scores))
            return scores[max_score_index], moves[max_score_index]
        else:
            min_score, min_score_index = min((score, idx) for idx, score in enumerate(scores))
            return scores[min_score_index], moves[min_score_index]
       
    
    def _score(self, winning_marker: Marker, depth: int) -> int:
        if winning_marker == self.current_marker():
            return 10 - depth
        elif winning_marker == self.opposite_marker():
            return depth - 10
        else:
            return 0
    
     
        
        
if __name__ == "__main__": 
    robot = AdvancedRobotPlayer(O)
    test_board = GameBoard()
    test_board.register(X, 1)
    test_board.register(O, 6)
    test_board.register(X, 5)
    test_board.register(O, 7)
    test_board.register(X, 8)
    score, next_move = robot.place_marker_on(test_board)
    print("AdvancedRobotPlayer's next move: " + str(next_move))
    