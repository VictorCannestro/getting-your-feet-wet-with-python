import copy
import random 
from functools import lru_cache
from tictactoe.domain.players.robot_player import RobotPlayer 
from tictactoe.domain.constants import Marker, X, O
from tictactoe.domain.gameboard.game_board import GameBoard


class AdvancedRobotPlayer(RobotPlayer):
    
    _INITIAL_DEPTH = 0
            
    
    def place_marker_on(self, board: GameBoard) -> int:
        """
        Uses the recursive Minimax Algorithm to generate an optimal next move.

        Parameters
        ----------
        board : GameBoard
            The current state of the game's board representation.

        Returns
        -------
        int
            An optimal position among the empty spaces on the board.
        """
        if board.is_empty():
            return random.choice(board.corner_positions())
        score, next_move = self._minimax(copy.deepcopy(board), self._INITIAL_DEPTH)
        return next_move
 
    
    @lru_cache()
    def _minimax(self, simulated_board: GameBoard, depth: int) -> tuple:
        """
        This is a n-move lookahead strategy. That is, it simulates and scores
        all possible next-move combinations until a game ending state has been
        reached.

        Parameters
        ----------
        board : GameBoard
            The current state of the game's board representation.
        depth : int
            The depth of the lookahead to consider during a recursive call--i.e.
            looking 0 moves ahead, 1 move ahead, 2 moves ahead, etc.

        Returns
        -------
        tuple
            Heuristic score of the optimal next move,
            Position of the optimal next move.
        """
        game_over, winner = simulated_board.determine_if_game_has_ended()
        if game_over:
            return self._score(winner, depth), None

        depth += 1
        scores, moves = [], []
        alternating_marker = self.current_marker() if depth % 2 == 1 else self.opposite_marker()      
        for possible_next_move in simulated_board.empty_spaces():  
            possible_game = copy.deepcopy(simulated_board)
            possible_game.register(alternating_marker, possible_next_move)
            scores.append(self._minimax(possible_game, depth)[0])
            moves.append(possible_next_move)
            
        if alternating_marker.symbol == self.current_marker().symbol:
            max_score, max_score_index = max((score, idx) for idx, score in enumerate(scores))
            return max_score, moves[max_score_index]
        else:
            min_score, min_score_index = min((score, idx) for idx, score in enumerate(scores))
            return min_score, moves[min_score_index]      

    
    def _score(self, winning_marker: Marker, depth: int) -> int:
        """
        Heuristic evaluation. This provides an arbitrary metric for the minimax
        algorithm to score different possible next moves.

        Parameters
        ----------
        winning_marker : Marker
            The winner marker, if applicable. Either X, O, or None.
        depth : int
            How many moves ahead needed to be simulated in order for a game 
            ending state to be reached.

        Returns
        -------
        int
            The final score of the n-move lookahead, adjusted for how deep the
            algorithm travelled to reach a game ending state. Shorter paths 
            receive "higher" scores.

        """
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
    