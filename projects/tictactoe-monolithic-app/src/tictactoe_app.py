#
# ▀█▀ █ █▀▀ ▀█▀ ▄▀█ █▀▀ ▀█▀ █▀█ █▀▀
# ░█░ █ █▄▄ ░█░ █▀█ █▄▄ ░█░ █▄█ ██▄
#
# https://fsymbols.com/text-art/

from collections import namedtuple
import random 


Decision = namedtuple("Decision", ["symbol"])
YES = Decision("y")
NO = Decision("n")

Marker = namedtuple("Marker", ["symbol"])
X = Marker("X")
O = Marker("O")
EMPTY = Marker("-")

Outcome = namedtuple("Outcome", ["is_game_over", "winner"])
X_WON = Outcome(True, X)
O_WON = Outcome(True, O)
DRAW = Outcome(True, None)
GAME_NOT_FINISHED = Outcome(False, None)


class PositionOccupied(Exception):
    pass


class CannotMakeMove(Exception):
    pass


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
    
        
    def __init__(self):
        self.board_map = self._blank_board()

    def display(self):
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
        
    def display_demo_board(self) -> None:
        print(self.__demo_board)
        
    def current_state(self) -> dict:
        return self.board_map
    
    def register(self, marker: Marker, position: int) -> None:
        if position not in range(10):
            raise ValueError("position must be an integer from 0 to 9.")            
        if marker.symbol not in [X.symbol, O.symbol]:
            raise ValueError(f"marker must be either an '{X.symbol}' or '{O.symbol}' Marker.")            
        if self.board_map.get(position) != EMPTY.symbol:
            raise PositionOccupied("Cannot place game_piece in an occupied position.")
        self.board_map[position] = marker.symbol
    
    
    def empty_spaces(self) -> dict:
        return self._filter_state_using(
            lambda position_marker_pair: position_marker_pair[1] == EMPTY.symbol, 
            self.current_state()
        )
    
    def spaces_occupied_by(self, marker: Marker) -> dict:
        if marker.symbol not in [X.symbol, O.symbol]:
            raise ValueError(f"marker must be either an '{X.symbol}' or '{O.symbol}' Marker")     
        return self._filter_state_using(
            lambda position_marker_pair: position_marker_pair[1] == marker.symbol, 
            self.current_state()
        )
    
    def reset(self) -> None:
        self.board_map = self._blank_board()
    
    def determine_if_game_has_ended(self) -> Decision:
        if self._win_conditions_reached_for(X):
            return X_WON
        if self._win_conditions_reached_for(O):
            return O_WON
        if not self.empty_spaces():
            return DRAW
        return GAME_NOT_FINISHED
    
    
    def _filter_state_using(self, filter_function, dictionary: dict) -> dict:
        return dict(filter(filter_function, dictionary.items()))
    
    def _win_conditions_reached_for(self, marker: Marker) -> bool:
        currently_held_positions = self.spaces_occupied_by(marker)
        for win_condition in self.__WIN_CONDITIONS:
            matching_positions = 0
            for position in currently_held_positions:
                if position in win_condition:
                    matching_positions += 1
            if matching_positions == 3:
                return True
        return False
    
    def _blank_board(self) -> dict:
        return {cell: EMPTY.symbol for cell in range(9)}        
            
    
class Player():

    __ADMISSABLE_POSITIONS = tuple(str(n) for n in range(9))

    
    def __init__(self, marker: Marker):
        self.marker = marker
        
    def current_marker(self) -> Marker:
        return self.marker
    
    def opposite_marker(self) -> Marker:
        return X if self.marker == O else O
    
    def set_marker(self, marker: Marker):
        self.marker = marker
        
    def place_marker_on(self, board: GameBoard) -> int:
        if not board.empty_spaces().keys():
            raise CannotMakeMove("An impossible state has been reached: The player has been prompted for a move, but there are no more playable moves.")
        player_input = input("Position of your next move: ")
        while not(self._in_admissable_positions(player_input) and self._position_is_available(int(player_input), board)):
            print("Not an available position. Choose again.")
            player_input = input("Position of your next move: ")
        return int(player_input)
    
    def _in_admissable_positions(self, player_input: str) -> bool:
        return player_input in self.__ADMISSABLE_POSITIONS
    
    def _position_is_available(self, position: int, board: GameBoard) -> bool:
        return position in board.empty_spaces().keys()
    
    def choose_next_marker(self) -> None:
        player_input = input(f"Winner's choice: '{X.symbol}' or '{O.symbol}'? ")
        while player_input not in [X.symbol, O.symbol]:
            print(f"Please enter either '{X.symbol}' or '{O.symbol}'")
            player_input = input(f"Your choice: '{X.symbol}' or '{O.symbol}'? ")
        self.set_marker(X if player_input == X.symbol else O)    
    
    def prompt_to_continue(self) -> bool:
        player_input = input(f"Would you like to play again? Enter [{YES.symbol}|{NO.symbol}] ")
        while player_input not in [YES.symbol, NO.symbol]:
            print(f"Please enter either [{YES.symbol}|{NO.symbol}]")
            player_input = input(f"Would you like to play again? Enter [{YES.symbol}|{NO.symbol}] ")
        return True if player_input == YES.symbol else False
    
    
class RobotPlayer():
    
    def __init__(self, marker: Marker):
        self.marker = marker
        
    def current_marker(self) -> Marker:
        return self.marker
    
    def opposite_marker(self) -> Marker:
        return X if self.marker == O else O
    
    def set_marker(self, marker: Marker) -> None:
        self.marker = marker
        
    def place_marker_on(self, board) -> int:
        available_positions = board.empty_spaces().keys()
        if not available_positions:
            raise CannotMakeMove("An impossible state has been reached: There are no available choices for the robot to make.") 
        available_indexable_positions = tuple(available_positions)
        choice = random.choice(available_indexable_positions)
        print(f"Robot selected position: {choice}")
        return choice
    
    def choose_next_marker(self) -> None:
        if self.current_marker() != X:
            self.set_marker(self.opposite_marker())
        print(f"\nRobot is {self.current_marker().symbol}")
    

class TicTacToeApp():
    
    __LOGO = """
▀█▀ █ █▀▀ ▀█▀ ▄▀█ █▀▀ ▀█▀ █▀█ █▀▀
░█░ █ █▄▄ ░█░ █▀█ █▄▄ ░█░ █▄█ ██▄
"""
    
    
    def __init__(self):
        print(self.__LOGO)
        print("How to win: get three markers in a row, column, or diagonal.")
        print("X goes first.")
        self.board = GameBoard()
        self.board.display_demo_board()
        self.human_player = Player(self._players_initial_choice())
        self.robot_player = RobotPlayer(self.human_player.opposite_marker())
        self.continue_playing = True
        
    def launch(self) -> None:
        while self.continue_playing:
            winner = None
            game_over = False
            while not game_over:
                if self.human_player.current_marker() == X:
                    self.board.display()
                    self.board.register(X, self.human_player.place_marker_on(self.board))
                    game_over, winner = self.board.determine_if_game_has_ended()
                    if game_over:
                        break
                    self.board.register(O, self.robot_player.place_marker_on(self.board))
                    game_over, winner = self.board.determine_if_game_has_ended()
                    if game_over:
                        break
                else:
                    self.board.register(X, self.robot_player.place_marker_on(self.board))
                    game_over, winner = self.board.determine_if_game_has_ended()
                    if game_over:
                        break
                    self.board.display()
                    self.board.register(O, self.human_player.place_marker_on(self.board))
                    game_over, winner = self.board.determine_if_game_has_ended()
                    if game_over:
                        break
            self._declare_game_results(winner)
            self.continue_playing = self.human_player.prompt_to_continue()
            if self.continue_playing:
                self._setup_new_game(winner)
        print("Thank you for playing.")
        
    def _players_initial_choice(self) -> Marker:
        if X.symbol == O.symbol:
            raise ValueError("Opposing players cannot have the same game markers.")
        player_input = input(f"Your choice: '{X.symbol}' or '{O.symbol}'? ")
        while player_input not in [X.symbol, O.symbol]:
            print(f"player_input enter either '{X.symbol}' or '{O.symbol}'")
            player_input = input(f"Your choice: '{X.symbol}' or '{O.symbol}'? ")
        return X if player_input == X.symbol else O
    
    def _declare_game_results(self, winner) -> None:
        self.board.display()
        if not winner:
            print("The game ended in a draw." )
        else:
            print(f"The game has ended. {winner.symbol} has won.")
    
    def _setup_new_game(self, winner) -> None:
        self.board.reset()
        if self.human_player.current_marker() == winner:
            self.human_player.choose_next_marker()
            self.robot_player.set_marker(self.human_player.opposite_marker())
        elif self.robot_player.current_marker() == winner:
            self.robot_player.choose_next_marker()
            self.human_player.set_marker(self.robot_player.opposite_marker())
        else:
            print("After a draw both players will keep their current markers.")
        print(f"Player is {self.human_player.current_marker().symbol}")
    

    
if __name__ == "__main__":
    app = TicTacToeApp()
    app.launch()