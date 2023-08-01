from tictactoe.domain.gameboard.game_board import GameBoard
from tictactoe.adapters.user_interface import UserInterface


class TextBasedUserInterface(UserInterface):

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
        print(self.__DEMO_BOARD)
        
    def display_current(self, board: GameBoard) -> None:
        current_state = board.current_state()
        print(f'''
   |   |   
 {current_state[0]} | {current_state[1]} | {current_state[2]} 
___|___|___
   |   |   
 {current_state[3]} | {current_state[4]} | {current_state[5]} 
___|___|___
   |   |   
 {current_state[6]} | {current_state[7]} | {current_state[8]} 
   |   |   ''')

    def display_the_rules(self) -> None:
        print("THE RULES:")
        print("\t1. This is a two player game where players alternate moves each turn.")
        print("\t2. The player with the 'X' marker goes first.")
        print("\t3. How to win: get three markers in a row, column, or diagonal.")
        print("\t4. The winner chooses which marker to play as next.")
        print("\t5. If there are no available positions on the board and there is not a winner, then the game is a draw.")
        print("\t6. After a draw both players keep their respective markers.")


if __name__ == "__main__": 
    pass