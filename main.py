def fibonacci(n):
    """Определяет n чисел Фибоначчи и возвращает их в виде списка."""
    if n <= 0:
        return []  # Возвращаем пустой список для некорректного n
    elif n == 1:
        return [0]  # Первое число Фибоначчи
    elif n == 2:
        return [0, 1]  # Первые два числа Фибоначчи

    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence


def bubble_sort(arr):
    """Сортирует переданный список чисел методом пузырька и возвращает отсортированную копию."""
    sorted_arr = arr[:]
    n = len(sorted_arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if sorted_arr[j] > sorted_arr[j+1]:
                sorted_arr[j], sorted_arr[j+1] = sorted_arr[j+1], sorted_arr[j]
    return sorted_arr


def calculator(num1, num2, operation):
    """Выполняет математическое действие между двумя числами в зависимости от операции."""
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            raise ValueError("Деление на ноль не допускается.")
        return num1 / num2
    else:
        raise ValueError("Некорректный оператор. Используйте +, -, *, /.")
