import os
import heapq


def dijkstra(n, graph, start, end):
    """Алгоритм Дейкстры для поиска кратчайшего пути"""
    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]  # (стоимость, узел)

    while pq:
        curr_cost, node = heapq.heappop(pq)

        if curr_cost > dist[node]:
            continue

        for neighbor, weight in graph[node]:
            new_cost = curr_cost + weight
            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))

    return dist[end] if dist[end] != INF else -1


def read_file(path):
    """Читает входные данные из файла"""
    with open(os.path.join(path, "input.txt"), "r") as file:
        return file.readlines()


def write_file(path, data):
    """Записывает выходные данные в файл"""
    with open(os.path.join(path, "output.txt"), "w") as file:
        file.writelines(data)


def main():
    path = os.path.dirname(os.path.abspath(__file__))
    lst = read_file(path)
    n, m = map(int, lst[0].split())
    graph = {i: [] for i in range(1, n + 1)}

    for i in range(1, m + 1):
        a, b, w = map(int, lst[i].split())
        graph[a].append((b, w))

    u, v = map(int, lst[m + 1].split())
    result = dijkstra(n, graph, u, v)
    write_file(path, [str(result) + "\n"])


if __name__ == "__main__":
    main()
