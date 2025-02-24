from itertools import product


def is_valid_pattern(grid, M, N):
    """Проверяет, нет ли в узоре квадрата 2×2 одного цвета."""
    for i in range(M - 1):
        for j in range(N - 1):
            # Проверяем 2×2 квадрат
            if grid[i][j] == grid[i + 1][j] == grid[i][j + 1] == grid[i + 1][j + 1]:
                return False
    return True


def count_beautiful_patterns(M, N):
    """Подсчитывает количество симпатичных узоров размером M×N."""
    total_count = 0

    # Перебираем все возможные расстановки плиток
    for bits in product([0, 1], repeat=M * N):
        # Преобразуем в двумерный массив (матрицу M×N)
        grid = [[bits[i * N + j] for j in range(N)] for i in range(M)]

        # Проверяем на "симпатичность"
        if is_valid_pattern(grid, M, N):
            total_count += 1

    return total_count


# Читаем входные данные
with open("input.txt", "r") as f:
    M, N = map(int, f.readline().split())

# Вычисляем количество симпатичных узоров
result = count_beautiful_patterns(M, N)

# Записываем результат
with open("output.txt", "w") as f:
    f.write(str(result) + "\n")
