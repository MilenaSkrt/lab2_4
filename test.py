import pytest
from biblioteca import fibonacci, bubble_sort, calculator

# Тестирование функции fibonacci
def test_fibonacci():
    assert fibonacci(0) == []
    assert fibonacci(1) == [0]
    assert fibonacci(2) == [0, 1]
    assert fibonacci(5) == [0, 1, 1, 2, 3]
    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Тестирование функции bubble_sort
def test_bubble_sort():
    assert bubble_sort([4, 3, 2, 1]) == [1, 2, 3, 4]
    assert bubble_sort([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert bubble_sort([]) == []
    assert bubble_sort([5]) == [5]
    assert bubble_sort([3, 1, 2, 3, 1]) == [1, 1, 2, 3, 3]

# Тестирование функции calculator
def test_calculator():
    assert calculator(2, 3, '+') == 5
    assert calculator(5, 3, '-') == 2
    assert calculator(2, 3, '*') == 6
    assert calculator(6, 3, '/') == 2
    with pytest.raises(ValueError, match="Деление на ноль не допускается."):
        calculator(6, 0, '/')
    with pytest.raises(ValueError, match="Некорректный оператор. Используйте +, -, *, /."):
        calculator(6, 3, '^')
