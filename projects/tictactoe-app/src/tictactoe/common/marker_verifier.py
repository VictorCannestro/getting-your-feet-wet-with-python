from tictactoe.domain.constants import Marker, X, O, AVAILABLE_MARKERS
from functools import wraps


def assume_marker_is_available(func):
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        verify_is_available(args[1])
        return func(*args, **kwargs)
    return wrapper_func

def verify_is_available(marker: Marker) -> bool:
    if marker.symbol not in AVAILABLE_MARKERS:
        raise ValueError(f"marker must be either an '{X.symbol}' or '{O.symbol}' Marker")               
    return True
         
def verify_markers_do_not_conflict(x: Marker, o: Marker) -> bool:                
    if x.symbol == o.symbol:
        raise ValueError("Opposing players cannot have the same game markers.")       
    return True
        

if __name__ == "__main__": 
    print("Working inside MarkerVerifier")