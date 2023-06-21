from main import operations_list, calculate


def test_sum_operation():
    operation = operations_list[0]
    result, error = calculate(1, 2, operation)
    assert error is None
    assert result == 3

    result, error = calculate(1, -2, operation)
    assert error is None
    assert result == -1

    result, error = calculate(0, 3, operation)
    assert error is None
    assert result == 3

    result, error = calculate(0, -3, operation)
    assert error is None
    assert result == -3

    result, error = calculate(5, 0, operation)
    assert error is None
    assert result == 5


def test_diff_operation():
    operation = operations_list[1]
    result, error = calculate(1, 2, operation)
    assert error is None
    assert result == -1

    result, error = calculate(1, -2, operation)
    assert error is None
    assert result == 3

    result, error = calculate(0, 3, operation)
    assert error is None
    assert result == -3

    result, error = calculate(0, -3, operation)
    assert error is None
    assert result == 3

    result, error = calculate(5, 0, operation)
    assert error is None
    assert result == 5


def test_multiply_operation():
    operation = operations_list[2]
    result, error = calculate(1, 2, operation)
    assert error is None
    assert result == 2

    result, error = calculate(1, -2, operation)
    assert error is None
    assert result == -2

    result, error = calculate(0, 3, operation)
    assert error is None
    assert result == 0

    result, error = calculate(0, -3, operation)
    assert error is None
    assert result == 0

    result, error = calculate(5, 0, operation)
    assert error is None
    assert result == 0


def test_divide_operation():
    operation = operations_list[3]
    result, error = calculate(1, 2, operation)
    assert error is None
    assert result == 0

    result, error = calculate(1, -2, operation)
    assert error is None
    assert result == 0

    result, error = calculate(0, 3, operation)
    assert error is None
    assert result == 0

    result, error = calculate(0, -3, operation)
    assert error is None
    assert result == 0

    result, error = calculate(5, 0, operation)
    assert error == 'Попытка делить на ноль'
    assert result is None


def test_unknown_operation():
    operation = 'дифференцирование'
    result, error = calculate(1, 2, operation)
    assert error == 'Неизвестный метод'
    assert result is None
