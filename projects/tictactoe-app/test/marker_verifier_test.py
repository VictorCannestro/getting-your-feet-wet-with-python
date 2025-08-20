import pytest

from tictactoe.common.marker_verifier import verify_is_available, verify_markers_do_not_conflict
from tictactoe.domain.constants import Marker, X, O


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

    @pytest.mark.parametrize("pair", [(X,X), (O,O), (Marker("D"), Marker("D"))])
    def test_conflicting_markers_should_raise_error(self, pair: tuple):
        a, b = pair
        with pytest.raises(ValueError) as exception_info: 
            verify_markers_do_not_conflict(a,b)
        assert exception_info     


if __name__ == "__main__": 
    pass
