from tictactoe.domain.constants import ADMISSABLE_POSITIONS, DIM
from tictactoe.domain.constants import Marker, X, O, EMPTY
from tictactoe.domain.constants import Outcome, X_WON, O_WON, DRAW, GAME_NOT_FINISHED
from tictactoe.domain.constants import ENOUGH_TO_WIN
from tictactoe.domain.exceptions import PositionOccupied
from tictactoe.common.position_verifier import assume_position_is_admissible
from tictactoe.common.marker_verifier import assume_marker_is_available


class GameBoard():  
        
    def __init__(self) -> None:
        self.board_map = self._blank_board()
        self.win_conditions = self.row_win_conditions() + self.column_win_conditions() + self.diagonal_win_conditions()

    def _blank_board(self) -> dict:
        return {cell: EMPTY.symbol for cell in ADMISSABLE_POSITIONS[::]} 
        
    def current_state(self) -> dict:
        return self.board_map
    
    @assume_position_is_admissible
    @assume_marker_is_available
    def register(self, marker: Marker, position: int) -> None:
        if self.board_map.get(position) != EMPTY.symbol:
            raise PositionOccupied("Cannot place game_piece in an occupied position.")
        self.board_map[position] = marker.symbol
        
    def is_empty(self) -> bool:
       return len(self.empty_spaces()) == len(ADMISSABLE_POSITIONS[::])
       
    def empty_spaces(self) -> tuple:
        return tuple(self._filter_state_using(
            lambda position_marker_pair: position_marker_pair[1] == EMPTY.symbol, 
            self.current_state()
        ))
    
    @assume_marker_is_available
    def spaces_occupied_by(self, marker: Marker) -> dict:
        return self._filter_state_using(
            lambda position_marker_pair: position_marker_pair[1] == marker.symbol, 
            self.current_state()
        )

    def _filter_state_using(self, filter_function: object, dictionary: dict) -> dict:
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
            if sum(matching_positions) == ENOUGH_TO_WIN.value:
                return True
        return False     

    def reset(self) -> None:
        self.board_map = self._blank_board()    
        
    def corner_positions(self) -> tuple:
        return (0, DIM.columns-1, DIM.columns*(DIM.rows-1), DIM.rows*DIM.columns-1)
    
    def row_win_conditions(self) -> list:
        if DIM.columns > DIM.rows:
            win_conditions = []
            number_of_win_conditions_per_row =  DIM.columns - DIM.rows + 1
            for i in range(DIM.rows):
                for index in range(number_of_win_conditions_per_row):
                    win_conditions.append(
                        tuple(i*DIM.columns + j + index for j in range(ENOUGH_TO_WIN.value))
                    )
            return win_conditions
        else:
            return [
                tuple(i*DIM.columns+j for j in range(ENOUGH_TO_WIN.value)) 
                for i in range(DIM.rows)
            ]
    
    def column_win_conditions(self) -> list:
        return [(0, 3, 6), (1, 4, 7), (2, 5, 8)]
    
    def diagonal_win_conditions(self) -> list:
        return [(0, 4, 8), (2, 4, 6)]
        
    def __str__(self) -> str:
        return f'''
   |   |   
 {self.board_map[0]} | {self.board_map[1]} | {self.board_map[2]} 
___|___|___
   |   |   
 {self.board_map[3]} | {self.board_map[4]} | {self.board_map[5]} 
___|___|___
   |   |   
 {self.board_map[6]} | {self.board_map[7]} | {self.board_map[8]} 
   |   |   '''
       
      
if __name__ == "__main__": 
    test_board = GameBoard()
    print(test_board.win_conditions)