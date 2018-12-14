import opera
import pytest

def test_operate():
    assert opera.operate(6, 8, '+')== 14, "failed on '+'"
    assert opera.operate(6, 8, '-')== -2, "failed on'-'"
    assert opera.operate(6, 8, '*')== 48, "failed on '*'"
    assert opera.operate(6, 8, '/')== 3/4, "failed on '/'"
    
    with pytest.raises(ZeroDivisionError) as err1:
        opera.operate(6, 0, '/')
    assert err1.value.args[0] == "division by zero is undefined"

    with pytest.raises(TypeError) as err2:
        opera.operate(6, 0, 0)
    assert err2.value.args[0] == "oper must be a string"

    with pytest.raises(ValueError) as err3:
        opera.operate(6, 0, '!=')
    assert err3.value.args[0] == "oper must be one of '+', '/', '-', or '*'"
