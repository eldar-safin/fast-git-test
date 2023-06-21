from main import methods_list, calculate

def test_sum_method():
    method = methods_list[0]
    result, error = calculate(1, 2, method)
    assert error is None
    assert result == 3

    result, error = calculate(1, -2, method)
    assert error is None
    assert result == -1

    result, error = calculate(0, 3, method)
    assert error is None
    assert result == 3

    result, error = calculate(0, -3, method)
    assert error is None
    assert result == -3

    result, error = calculate(5, 0, method)
    assert error is None
    assert result == 5

def test_diff_method():
    method = methods_list[1]
    result, error = calculate(1, 2, method)
    assert error is None
    assert result == -1

    result, error = calculate(1, -2, method)
    assert error is None
    assert result == 3

    result, error = calculate(0, 3, method)
    assert error is None
    assert result == -3

    result, error = calculate(0, -3, method)
    assert error is None
    assert result == 3

    result, error = calculate(5, 0, method)
    assert error is None
    assert result == 5

def test_multp_method():
    method = methods_list[2]
    result, error = calculate(1, 2, method)
    assert error is None
    assert result == 2

    result, error = calculate(1, -2, method)
    assert error is None
    assert result == -2

    result, error = calculate(0, 3, method)
    assert error is None
    assert result == 0

    result, error = calculate(0, -3, method)
    assert error is None
    assert result == 0

    result, error = calculate(5, 0, method)
    assert error is None
    assert result == 0


def test_divide_method():
    method = methods_list[3]
    result, error = calculate(1, 2, method)
    assert error is None
    assert result == 0

    result, error = calculate(1, -2, method)
    assert error is None
    assert result == 0

    result, error = calculate(0, 3, method)
    assert error is None
    assert result == 0

    result, error = calculate(0, -3, method)
    assert error is None
    assert result == 0

    result, error = calculate(5, 0, method)
    assert error == 'Попытка делить на ноль'
    assert result is None

def test_unknown_method():
    method = 'дифференцирование'
    result, error = calculate(1, 2, method)
    assert error == 'Неизвестный метод'
    assert result is None
