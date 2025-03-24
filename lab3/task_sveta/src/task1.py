from collections import deque
from utils import utils
import os

PATH = os.path.dirname(os.path.abspath(__file__))


def bfs(graph, start, end, n):
    # Массив для отслеживания посещённых вершин
    visited = [False] * (n + 1)

    # Очередь для BFS
    queue = deque([start])
    visited[start] = True

    while queue:
        current = queue.popleft()

        # Если мы достигли конечной вершины, возвращаем True
        if current == end:
            return True

        # Добавляем в очередь все соседние вершины, которые ещё не посещены
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    # Если не нашли путь, возвращаем False
    return False


def solve():
    # Чтение входных данных из файла
    lst = utils.read_file(PATH)

    # Получаем количество вершин и рёбер
    n, m = map(int, lst[0].split())

    # Создаём граф (список смежности)
    graph = [[] for _ in range(n + 1)]

    # Чтение рёбер
    for i in range(1, m + 1):
        u, v = utils.str_to_list(lst[i])
        graph[u].append(v)
        graph[v].append(u)

    # Чтение двух вершин, между которыми проверяем наличие пути
    start, end = utils.str_to_list(lst[m + 1])

    # Проверяем, есть ли путь между start и end
    result = 1 if bfs(graph, start, end, n) else 0

    # Записываем результат в файл
    utils.write_file(PATH, data=[result])


if __name__ == "__main__":
    solve()
