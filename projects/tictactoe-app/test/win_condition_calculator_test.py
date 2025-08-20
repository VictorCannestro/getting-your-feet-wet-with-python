import pytest
from tictactoe.domain.gameboard.win_condition_calculator import WinConditionCalculator
from tictactoe.domain.constants import Dimensions


class WinConditionCalculatorTest(object):
    
    test_dimensions = [Dimensions(3,3), Dimensions(3,4), Dimensions(4,3)]
    
    test_row_win_conditions = [
        [(0, 1, 2), (3, 4, 5), (6, 7, 8)],                                     # SQUARE
        [(0, 1, 2), (1, 2, 3), (4, 5, 6), (5, 6, 7), (8, 9, 10), (9, 10, 11)], # WIDE
        [(0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11)]                         # TALL  
    ]
    
    test_column_win_conditions = [
        [(0, 3, 6), (1, 4, 7), (2, 5, 8)],                                     # SQUARE
        [(0, 4, 8), (1, 5, 9), (2, 6, 10), (3, 7, 11)],                        # WIDE
        [(0, 3, 6), (1, 4, 7), (2, 5, 8), (3, 6, 9), (4, 7, 10), (5, 8, 11)]   # TALL  
    ] 
    
    test_diagonal_win_conditions = [
        [(0, 4, 8), (2, 4, 6)],                         # SQUARE
        [(0, 5, 10), (1, 6, 11), (2, 5, 8), (3, 6, 9)], # WIDE
        [(0, 4, 8), (3, 7, 11), (2, 4, 6), (5, 7, 9)]   # TALL  
    ] 
    
    
    def test_standard_game_win_conditions(self):
        actual = WinConditionCalculator(Dimensions(3,3)).calculate_win_conditions()
        expected = [(0, 1, 2), (3, 4, 5), (6, 7, 8)] + [(0, 3, 6), (1, 4, 7), (2, 5, 8)] + [(0, 4, 8), (2, 4, 6)]
        message = f"Expected {expected} but got {actual}"
        assert len(actual) == len(expected), message 
        assert set(actual) == set(expected), message              
        
    @pytest.mark.parametrize("dimensions, rows", zip(test_dimensions, test_row_win_conditions))
    def test_row_win_conditions(self, dimensions, rows):
        calculator = WinConditionCalculator(dimensions)
        n, m = dimensions.rows, dimensions.columns
        actual = calculator.win_conditions_by_rows(n, m, min(n,m))
        expected = rows
        message = f"Expected {expected} but got {actual}"
        assert len(actual) == len(expected), message 
        assert set(actual) == set(expected), message  
        
    @pytest.mark.parametrize("dimensions, columns", zip(test_dimensions, test_column_win_conditions))
    def test_column_win_conditions(self, dimensions, columns):
        calculator = WinConditionCalculator(dimensions)
        n, m = dimensions.rows, dimensions.columns
        actual = calculator.win_conditions_by_columns(n, m, min(n,m))
        expected = columns 
        message = f"Expected {expected} but got {actual}"
        assert len(actual) == len(expected), message 
        assert set(actual) == set(expected), message  
        
    @pytest.mark.parametrize("dimensions, diagonals", zip(test_dimensions, test_diagonal_win_conditions))
    def test_diagonal_win_conditions(self, dimensions, diagonals):
        calculator = WinConditionCalculator(dimensions)
        n, m = dimensions.rows, dimensions.columns
        actual = calculator.win_conditions_by_diagonals(n, m, min(n,m))
        expected = diagonals
        message = f"Expected {expected} but got {actual}"
        assert len(actual) == len(expected), message 
        assert set(actual) == set(expected), message  