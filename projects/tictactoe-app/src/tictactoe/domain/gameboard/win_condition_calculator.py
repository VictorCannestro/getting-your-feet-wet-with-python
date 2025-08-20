from tictactoe.domain.constants import Dimensions, SQUARE, TALL
from tictactoe.domain.gameboard.board_type_mappings import determine_boardtype


class WinConditionCalculator:

    def __init__(self, dimensions: Dimensions) -> None:
        self.dimensions = dimensions

    def calculate_victory_threshold(self):
        return min(self.dimensions.rows, self.dimensions.columns)
    
    def calculate_win_conditions(self) -> list:
        n, m = self.dimensions.rows, self.dimensions.columns
        enough_to_win = self.calculate_victory_threshold()
        return self.win_conditions_by_rows(n, m, enough_to_win) + self.win_conditions_by_columns(n, m, enough_to_win) + self.win_conditions_by_diagonals(n, m, enough_to_win)
       
    def win_conditions_by_rows(self, n: int, m: int, enough_to_win: int) -> list:
        f = lambda x,y,z: x*y + z
        boardtype = determine_boardtype(n, m)
        if boardtype == SQUARE or boardtype == TALL: 
            return [tuple(f(i, m, j) for j in range(enough_to_win)) for i in range(n)]        
        else:
            win_conditions = []
            win_conditions_per_row = m-n+1
            for i in range(n):
                for index in range(win_conditions_per_row):
                    win_conditions.append(tuple(f(i, m, j+index) for j in range(enough_to_win)))
            return win_conditions
 
    def win_conditions_by_columns(self, n: int, m: int, enough_to_win: int) -> list:
        f = lambda x,y,z: x*y + z
        boardtype = determine_boardtype(n, m)
        if boardtype == SQUARE or boardtype == TALL: 
            return [tuple(f(j, m, i) for j in range(enough_to_win)) for i in range(n*(abs(m-n)+1))]           
        else:
            return [tuple(f(j, m, i) for j in range(enough_to_win)) for i in range(n)]
    
    def win_conditions_by_diagonals(self, n: int, m: int, enough_to_win: int) -> list:
        boardtype = determine_boardtype(n, m)
        win_conditions = []
        number_of_win_conditions_per_direction = abs(m-n)+1
        for i in range(number_of_win_conditions_per_direction):
            forward_diagonal, backward_diagonal = [], []
            for j in range(enough_to_win):
                if boardtype == SQUARE or boardtype == TALL:    
                    forward_diagonal.append(m*j + j + m*i)
                    backward_diagonal.append((min(m,n)-1)*(j+1) + m*i)
                else:
                    forward_diagonal.append(m*j + j + i)
                    backward_diagonal.append((min(m,n)-1)*(j+1) + i)        
            win_conditions.append(tuple(forward_diagonal))
            win_conditions.append(tuple(backward_diagonal))
        return win_conditions
