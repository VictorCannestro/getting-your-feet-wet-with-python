import pytest
from src.tictactoe.domain.constants import Marker, X, O
from src.tictactoe.common.marker_verifier import verify_is_available, verify_markers_do_not_conflict, pick_from



class VerifyIsAvailableTest(object):
    def test_X_is_available(self):
        assert verify_is_available(X) == True
        
    def test_O_is_available(self):
        assert verify_is_available(O) == True
        
    def test_nonXO_marker_not_available(self):
        D = Marker("D")
        with pytest.raises(ValueError) as exception_info: 
            verify_is_available(D)
        assert exception_info 
        

class VerifyMarkersDoNotConflictTest(object):
    def test_XO_constants_do_not_conflict(self):
        assert verify_markers_do_not_conflict(X,O) == True
        
    def test_OX_constants_do_not_conflict(self):
        assert verify_markers_do_not_conflict(O,X) == True

    def test_conflicting_markers_should_raise_error(self):
        D = Marker("D")
        E = Marker("D")
        with pytest.raises(ValueError) as exception_info: 
            verify_markers_do_not_conflict(D,E)
        assert exception_info 
        

class PickFromTest(object):
    pass



if __name__ == "__main__": 
    pass
