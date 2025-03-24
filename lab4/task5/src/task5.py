"""Постройте префикс-функцию для всех непустых префиксов заданной строки s."""

from utils import utils
import os

PATH = os.path.dirname(os.path.abspath(__file__))


def build_prefix(s: str) -> list:
    """
    Вычисляет префикс-функцию для заданной строки s.

    Args:
       s: Строка, для которой нужно вычислить префикс-функцию.

    Returns:
       Список, содержащий значения префикс-функции для всех префиксов строки s.
    """

    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j

    return pi


def main():
    lst = utils.read_file(PATH)
    s1 = lst[0]
    s2 = lst[1]
    result1 = build_prefix(s1)
    result2 = build_prefix(s2)
    return [result1, result2]


if __name__ == "__main__":
    result = main()
    utils.write_file(PATH, result)
