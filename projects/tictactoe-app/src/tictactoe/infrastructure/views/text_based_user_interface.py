from tictactoe.domain.gameboard.game_board import GameBoard
from tictactoe.common.position_verifier import admissible_str_positions
from tictactoe.adapters.inbound.user_interactable import UserInteractable
from tictactoe.adapters.outbound.displayable import Displayable


class TextBasedUserInterface(Displayable, UserInteractable):

    __LOGO = """
▄▄▄█████▓ ██▓ ▄████▄  ▄▄▄█████▓ ▄▄▄       ▄████▄  ▄▄▄█████▓ ▒█████  ▓█████ 
▓  ██▒ ▓▒▓██▒▒██▀ ▀█  ▓  ██▒ ▓▒▒████▄    ▒██▀ ▀█  ▓  ██▒ ▓▒▒██▒  ██▒▓█   ▀ 
▒ ▓██░ ▒░▒██▒▒▓█    ▄ ▒ ▓██░ ▒░▒██  ▀█▄  ▒▓█    ▄ ▒ ▓██░ ▒░▒██░  ██▒▒███   
░ ▓██▓ ░ ░██░▒▓▓▄ ▄██▒░ ▓██▓ ░ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒░ ▓██▓ ░ ▒██   ██░▒▓█  ▄ 
  ▒██▒ ░ ░██░▒ ▓███▀ ░  ▒██▒ ░  ▓█   ▓██▒▒ ▓███▀ ░  ▒██▒ ░ ░ ████▓▒░░▒████▒
  ▒ ░░   ░▓  ░ ░▒ ▒  ░  ▒ ░░    ▒▒   ▓▒█░░ ░▒ ▒  ░  ▒ ░░   ░ ▒░▒░▒░ ░░ ▒░ ░
    ░     ▒ ░  ░  ▒       ░      ▒   ▒▒ ░  ░  ▒       ░      ░ ▒ ▒░  ░ ░  ░
  ░       ▒ ░░          ░        ░   ▒   ░          ░      ░ ░ ░ ▒     ░   
          ░  ░ ░                     ░  ░░ ░                   ░ ░     ░  ░
             ░                           ░                                     
"""

    __DEMO_BOARD = '''
   |   |   
 0 | 1 | 2 
___|___|___
   |   |   
 3 | 4 | 5 
___|___|___
   |   |   
 6 | 7 | 8 
   |   |   '''    
   

    def display_logo(self) -> None:
        print(self.__LOGO)
   
    def display_demo_board(self) -> None:
        print("/nGAMEBOARD KEY:")
        print(self.__DEMO_BOARD)
        
    def display_current(self, board: GameBoard) -> None:
        print(board)

    def display_the_rules(self) -> None:
        print("THE RULES:")
        print(" 1. This is a two player game where players alternate moves each turn.")
        print(" 2. The player with the 'X' marker goes first.")
        print(" 3. Players can only place their marker in an empty position.")
        print(" 4. How to win: get three markers in a row, column, or diagonal.")
        print(" 5. The winner chooses which marker to play as next.")
        print(" 6. If there are no available positions on the board and there is not a winner, then the game is a draw.")
        print(" 7. After a draw both players keep their respective markers.")

    def pick_from(self, available_markers: tuple) -> str:
        x, o = available_markers
        player_input = input(f"Your choice: '{x}' or '{o}'? ")    
        while player_input not in available_markers:
            print(f"player_input enter either '{x}' or '{o}'")
            player_input = input(f"Your choice: '{x}' or '{o}'? ")
        return player_input
    
    def decide_from(self, available_decisions: tuple) -> str:
        yes, no = available_decisions
        player_input = input(f"Would you like to play again? Enter [{yes}|{no}] ")
        while player_input not in available_decisions:
            print(f"Please enter either [{yes}|{no}]")
            player_input = input(f"Would you like to play again? Enter [{yes}|{no}] ")    
        return player_input

    def select_position_from(self, board) -> int:
        player_input = input(f"Position of your next move {list(board.empty_spaces())}: ")
        while not(player_input in admissible_str_positions() and int(player_input) in board.empty_spaces()):
            print("Not an available position. Choose again.")
            player_input = input(f"Position of your next move {list(board.empty_spaces())}: ")
        return int(player_input)
    

if __name__ == "__main__": 
    pass