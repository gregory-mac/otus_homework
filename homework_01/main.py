"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    result = []
    for num in args:
        result.append(num ** 2)
    return result


def is_odd(number):
    return number % 2 == 1


def is_even(number):
    return number % 2 == 0


def is_prime(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True
    else:
        return None


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(num_list, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    result = None
    if filter_type == ODD:
        result = list(filter(is_odd, num_list))
    if filter_type == EVEN:
        result = list(filter(is_even, num_list))
    if filter_type == PRIME:
        result = list(filter(is_prime, num_list))
    return result
