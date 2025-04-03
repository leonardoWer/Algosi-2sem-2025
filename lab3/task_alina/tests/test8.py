import unittest
import datetime
from lab3.task_alina.src.task8 import dijkstra

class TestFlightCost(unittest.TestCase):
    print("Lab3 task8 test")

    def test_1(self):
        # given
        input_data = """4 4
1 2 1
4 1 2
2 3 2
1 3 5
1 3"""
        expected_result = 3
        expected_time = 4

        # Когда данные передаются напрямую
        lines = input_data.splitlines()
        n, m = map(int, lines[0].split())
        graph = {i: [] for i in range(1, n + 1)}

        for i in range(1, m + 1):
            a, b, w = map(int, lines[i].split())
            graph[a].append((b, w))

        u, v = map(int, lines[m + 1].split())

        # when
        start_time = datetime.datetime.now()
        result = dijkstra(n, graph, u, v)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест1.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_2(self):
        # given
        input_data = """5 9
1 2 4
1 3 2
2 3 2
3 2 1
2 4 2
3 5 4
5 4 1
2 5 3
3 4 4
1 5"""
        expected_result = 6
        expected_time = 4

        # Когда данные передаются напрямую
        lines = input_data.splitlines()
        n, m = map(int, lines[0].split())
        graph = {i: [] for i in range(1, n + 1)}

        for i in range(1, m + 1):
            a, b, w = map(int, lines[i].split())
            graph[a].append((b, w))

        u, v = map(int, lines[m + 1].split())

        # when
        start_time = datetime.datetime.now()
        result = dijkstra(n, graph, u, v)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест2.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_3(self):
        # given
        input_data = """3 3
1 2 7
1 3 5
2 3 2
3 2"""
        expected_result = -1
        expected_time = 4

        # Когда данные передаются напрямую
        lines = input_data.splitlines()
        n, m = map(int, lines[0].split())
        graph = {i: [] for i in range(1, n + 1)}

        for i in range(1, m + 1):
            a, b, w = map(int, lines[i].split())
            graph[a].append((b, w))

        u, v = map(int, lines[m + 1].split())

        # when
        start_time = datetime.datetime.now()
        result = dijkstra(n, graph, u, v)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест3.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

if __name__ == '__main__':
    unittest.main()
