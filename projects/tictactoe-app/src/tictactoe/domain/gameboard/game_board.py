from tictactoe.domain.constants import ADMISSABLE_POSITIONS
from tictactoe.domain.constants import Marker, X, O, EMPTY
from tictactoe.domain.constants import Decision, X_WON, O_WON, DRAW, GAME_NOT_FINISHED
from tictactoe.domain.constants import ENOUGH_TO_WIN
from tictactoe.domain.exceptions import PositionOccupied
from tictactoe.common.position_verifier import verify_is_admissible
from tictactoe.common.marker_verifier import verify_is_available


class GameBoard():
    
    __THREE_IN_A_ROW = ((0, 1, 2), (3, 4, 5), (6, 7, 8))
    __THREE_IN_A_COLUMN = ((0, 3, 6), (1, 4, 7), (2, 5, 8)) 
    __THREE_IN_A_DIAGONAL = ((0, 4, 8), (2, 4, 6))
    __WIN_CONDITIONS = __THREE_IN_A_ROW + __THREE_IN_A_COLUMN + __THREE_IN_A_DIAGONAL

    __demo_board = '''
   |   |   
 0 | 1 | 2 
___|___|___
   |   |   
 3 | 4 | 5 
___|___|___
   |   |   
 6 | 7 | 8 
   |   |   '''
    
        
    def __init__(self) -> None:
        self.board_map = self._blank_board()

    def _blank_board(self) -> dict:
        return {cell: EMPTY.symbol for cell in self.admissible_positions()} 
        
    def admissible_positions(self):
        return ADMISSABLE_POSITIONS[::]
        
    def current_state(self) -> dict:
        return self.board_map
    
    def register(self, marker: Marker, position: int) -> None:
        verify_is_available(marker) 
        verify_is_admissible(position)                    
        if self.board_map.get(position) != EMPTY.symbol:
            raise PositionOccupied("Cannot place game_piece in an occupied position.")
        self.board_map[position] = marker.symbol
        
    def is_empty(self) -> bool:
       return len(self.empty_spaces()) == len(self.admissible_positions())
       
    def empty_spaces(self) -> tuple:
        return tuple(self._filter_state_using(
            lambda position_marker_pair: position_marker_pair[1] == EMPTY.symbol, 
            self.current_state()
        ))
    
    def spaces_occupied_by(self, marker: Marker) -> dict:
        verify_is_available(marker)     
        return self._filter_state_using(
            lambda position_marker_pair: position_marker_pair[1] == marker.symbol, 
            self.current_state()
        )

    def _filter_state_using(self, filter_function: object, dictionary: dict) -> dict:
        return dict(filter(filter_function, dictionary.items()))
    
    def corner_positions(self) -> tuple:
        return (0, 2, 6, 8)
    
    def determine_if_game_has_ended(self) -> Decision:
        if self._win_conditions_reached_for(X):
            return X_WON
        if self._win_conditions_reached_for(O):
            return O_WON
        if not self.empty_spaces():
            return DRAW
        return GAME_NOT_FINISHED
      
    def _win_conditions_reached_for(self, marker: Marker) -> bool:
        verify_is_available(marker)   
        currently_held_positions = self.spaces_occupied_by(marker)
        for win_condition in self.__WIN_CONDITIONS:
            matching_positions = (position in win_condition for position in currently_held_positions)   
            if sum(matching_positions) == ENOUGH_TO_WIN.value:
                return True
        return False     

    def reset(self) -> None:
        self.board_map = self._blank_board()
        
    def display_demo_board(self) -> None:
        print(self.__demo_board)
        
    def display(self) -> None:
        print(f'''
   |   |   
 {self.board_map[0]} | {self.board_map[1]} | {self.board_map[2]} 
___|___|___
   |   |   
 {self.board_map[3]} | {self.board_map[4]} | {self.board_map[5]} 
___|___|___
   |   |   
 {self.board_map[6]} | {self.board_map[7]} | {self.board_map[8]} 
   |   |   ''')
       
      
if __name__ == "__main__": 
    test_board = GameBoard()
    test_board.display_demo_board()