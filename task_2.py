"""
Задача 2. Дан массив целых чисел. Нужно удалить из него нули.
Можно использовать только О(1) дополнительной памяти.
"""
from typing import List


def remove_zeros(a: List[int]) -> List[int]:
    """
    Работает за O(n)
    """
    n = 0
    for i in range(len(a)):
        if a[i] != 0:
            a[n] = a[i]
            n += 1
    return a[: n]
