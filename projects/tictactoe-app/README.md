# Tic-Tac-Toe
## Installation
### Frist Time Setup

For first time use, open up a fresh powershell and work through the following commands:
```bash
cd ~
mkdir virtual_environments
cd virtual_environments
python -m venv appvenv
 . appvenv/Scripts/activate
```

Now that we've activated the virtual environment, the subsequent terminal commands should start with `(appvenv)`. **Switch into the root directory containing our `getting-your-feet-wet-with-python` project** and run the following:
```bash 
cd projects\tictactoe-app
```
```bash
pip install .
```
```bash
python .\src\tictactoe\tic_tac_toe_app.py
```
If all went well, then the application should launch with the following screen:
![text-ui](../../../figures/tictactoe-text-based-ui.png)

To leave the virtual environment simply type
```bash
deactivate appvenv
```
This will return us from `(appvenv)` to `base` in the shell.

### Running the Application After First Time Setup
```bash
cd ~
cd virtual_environments
 . appvenv/Scripts/activate
```
**Switch into the directory containing our `getting-your-feet-wet-with-python\projects\tictactoe-app` folder**
```bash
python .\src\tictactoe\tic_tac_toe_app.py
```

## Requirements
##### 1:  There will be two players, one human and one computer.
##### 2:  The only valid symbols allowed on the board are 'X', 'O', and '_'.
##### 3: One player will be assigned X and the other, O.
##### 4: The human player will choose to play X or O for the first game.
##### 5: In each game afterwards, the most recent winner will choose to play X or O.
##### 6: When a new game starts, all cells on the game board should be blank.
##### 7: The player assigned X will make the first move.
##### 8: After the first move, the players will alternate turns.
##### 9: On one player's turn, that player will place their assigned symbol into a blank cell.
##### 10: Once played, that X or O shall remain in that cell until the end of the game.
##### 11: The first player to place three of their symbols in a row, column, or diagonal will be the winner.
##### 12: When no blank squares remain and neither player has won, the game is a draw.
