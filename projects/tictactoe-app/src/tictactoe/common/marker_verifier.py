from tictactoe.domain.constants import Marker, X, O, AVAILABLE_MARKERS


def verify_is_available(marker: Marker) -> bool:
    if marker.symbol not in AVAILABLE_MARKERS:
        raise ValueError(f"marker must be either an '{X.symbol}' or '{O.symbol}' Marker")               
    return True
         
def verify_markers_do_not_conflict(x: Marker, o: Marker) -> bool:                
    if x.symbol == o.symbol:
        raise ValueError("Opposing players cannot have the same game markers.")       
    return True
        
def pick_from(available_markers: tuple) -> str:
    x, o = available_markers
    player_input = input(f"Your choice: '{x}' or '{o}'? ")    
    while player_input not in available_markers:
        print(f"player_input enter either '{x}' or '{o}'")
        player_input = input(f"Your choice: '{x}' or '{o}'? ")
    return player_input


if __name__ == "__main__": 
    print("Working inside MarkerVerifier")