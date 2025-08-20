from importlib.util import source_hash

from tictactoe.domain.constants import Dimensions
from tictactoe.domain.constants import Marker, X, O, EMPTY
from tictactoe.domain.constants import Outcome, X_WON, O_WON, DRAW, GAME_NOT_FINISHED
from tictactoe.domain.exceptions import PositionOccupied
from tictactoe.domain.gameboard.win_condition_calculator import WinConditionCalculator
from tictactoe.common.position_verifier import assume_position_is_admissible
from tictactoe.common.marker_verifier import assume_marker_is_available


class GameBoard:
        
    def __init__(self, dimensions: Dimensions = Dimensions(3, 3)) -> None:
        self.dimensions = dimensions
        self.board_map = self._blank_board()
        self.calculator = WinConditionCalculator(dimensions)
        self.enough_to_win = self.calculator.calculate_victory_threshold()
        self.win_conditions = self.calculator.calculate_win_conditions()
    
    def _blank_board(self) -> dict:
        return {cell: EMPTY for cell in self.admissible_positions()[::]}

    def admissible_positions(self) -> range:
        return range(self.dimensions.rows * self.dimensions.columns)

    def reset(self) -> None:
        self.board_map = self._blank_board()    

    def current_state(self) -> dict:
        return self.board_map

    @assume_position_is_admissible
    @assume_marker_is_available
    def register(self, marker: Marker, position: int) -> None:
        if self.board_map.get(position) != EMPTY:
            raise PositionOccupied("Cannot place game piece in an occupied position.")
        self.board_map[position] = marker
        
    def is_empty(self) -> bool:
       return len(self.empty_spaces()) == len(self.admissible_positions()[::])
       
    def empty_spaces(self) -> tuple:
        return tuple(self._filter_state_using(lambda position_marker_pair:
            lambda position, assigned_marker: assigned_marker == EMPTY,
            self.current_state()
        ))
    
    @assume_marker_is_available
    def spaces_occupied_by(self, marker: Marker) -> dict:
        return self._filter_state_using(lambda position_marker_pair:
            lambda position, assigned_marker: assigned_marker == marker,
            self.current_state()
        )

    def _filter_state_using(self, filter_function, dictionary: dict) -> dict:
        return dict(filter(filter_function, dictionary.items()))
    
    def determine_if_game_has_ended(self) -> Outcome:
        if self._win_conditions_reached_for(X):
            return X_WON
        if self._win_conditions_reached_for(O):
            return O_WON
        if not self.empty_spaces():
            return DRAW
        return GAME_NOT_FINISHED
      
    @assume_marker_is_available    
    def _win_conditions_reached_for(self, marker: Marker) -> bool:
        currently_held_positions = self.spaces_occupied_by(marker)
        for win_condition in self.win_conditions:
            matching_positions = (position in win_condition for position in currently_held_positions)   
            if sum(matching_positions) == self.enough_to_win:
                return True
        return False     
        
    def corner_positions(self) -> tuple:
        return (
            0,
            self.dimensions.columns - 1,
            self.dimensions.columns * (self.dimensions.rows - 1),
            self.dimensions.rows * self.dimensions.columns - 1
        )
    
    def __str__(self) -> str:
        return f'''
   |   |   
 {self.board_map[0].symbol} | {self.board_map[1].symbol} | {self.board_map[2].symbol} 
___|___|___
   |   |   
 {self.board_map[3].symbol} | {self.board_map[4].symbol} | {self.board_map[5].symbol} 
___|___|___
   |   |   
 {self.board_map[6].symbol} | {self.board_map[7].symbol} | {self.board_map[8].symbol} 
   |   |   '''
       
      
if __name__ == "__main__": 
    test_board = GameBoard(Dimensions(3, 3))
    print(test_board.empty_spaces())
    print(test_board.win_conditions)