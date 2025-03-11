from itertools import product
from utils import utils
import os


PATH = os.path.dirname(os.path.abspath(__file__))


def is_valid_pattern(grid, M, N):
    """Проверяет, нет ли в узоре квадрата 2×2 одного цвета."""
    for i in range(M - 1):
        for j in range(N - 1):
            # Проверяем 2×2 квадрат, равны ли все цвета каждого элемента
            if grid[i][j] == grid[i + 1][j] == grid[i][j + 1] == grid[i + 1][j + 1]:
                # Если они равны, значить узор не является "симпатичным"
                return False
    # В противном случае все хорошо, узор подходит
    return True


def count_beautiful_patterns(M, N):
    """Подсчитывает количество симпатичных узоров, чтобы узнать, сколько клиентов можно будет обслужить"""
    total_count = 0

    # генерируем и перебираем все возможные варианты расстановки плиток
    for bits in product([0, 1], repeat=M * N):
        # создаем матрицу MxN (выкладываем плитки) (двумерный массив)
        grid = [[bits[i * N + j] for j in range(N)] for i in range(M)]

        # Проверяем на "симпатичность"
        if is_valid_pattern(grid, M, N):
            total_count += 1

    return total_count


if __name__ == "__main__":
    lst1 = utils.read_file(PATH)[0].split()
    lst2 = utils.read_file(PATH)[1].split()
    M1, N1, M2, N2 = int(lst1[0]), int(lst1[1]), int(lst2[0]), int(lst2[1])
    result1 = count_beautiful_patterns(M1, N1)
    result2 = count_beautiful_patterns(M2, N2)
    utils.write_file(PATH, [result1, result2])
