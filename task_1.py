"""
Задача 1.
Даны два списка, нужно вернуть элементы, которые есть в 1-ом списке, но нет во 2-ом.
Оценить эффективность своего решения.
"""
from typing import List


def get_diff(a: List[int], b: List[int]) -> List[int]:
    """
    Это решение в лоб. Оно работает за O(N^2).
    """
    result = []
    for i in a:
        if i not in b:
            result.append(i)
    return result


def get_diff(a: List[int], b: List[int]) -> List[int]:
    """
    Если заведем set(по сути хеш-таблица), то можно снизить до O(n)
    """
    result = []
    set_b = set(b)
    for i in a:
        if i not in set_b:
            result.append(i)
    return result
