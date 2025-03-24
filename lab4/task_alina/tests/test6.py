import unittest
import datetime
import os
from lab4.task_alina.src.task6 import z_function  # Замените на ваш модуль

class TestZFunction(unittest.TestCase):
    print("Z-Function Tests")

    def setUp(self):
        # Создаем временные файлы для тестов
        self.test_files = {
            "test1_input.txt": "aaaAAA",
            "test1_output.txt": "2 1 0 0 0",
            "test2_input.txt": "abacaba",
            "test2_output.txt": "0 1 0 3 0 1"
        }
        for filename, content in self.test_files.items():
            with open(filename, 'w') as f:
                f.write(content)

    def tearDown(self):
        # Удаляем временные файлы после тестов
        for filename in self.test_files:
            if os.path.exists(filename):
                os.remove(filename)

    def test_z_function_case1(self):
        # given
        input_file = "test1_input.txt"
        expected_output = "2 1 0 0 0"
        expected_time = 2  # Ожидаемое время в секундах

        # when
        start_time = datetime.datetime.now()
        with open(input_file, 'r') as file:
            s = file.readline().strip()
        z = z_function(s)
        result = " ".join(map(str, z[1:]))
        finish_time = datetime.datetime.now()
        result_time = (finish_time - start_time).total_seconds()
        print(f"Тест1. Время выполнения: {result_time} сек")

        # then
        self.assertEqual(result, expected_output)
        self.assertLessEqual(result_time, expected_time,
                            f"Время {result_time} сек превысило порог {expected_time} сек")

    def test_z_function_case2(self):
        # given
        input_file = "test2_input.txt"
        expected_output = "0 1 0 3 0 1"
        expected_time = 2  # Ожидаемое время в секундах

        # when
        start_time = datetime.datetime.now()
        with open(input_file, 'r') as file:
            s = file.readline().strip()
        z = z_function(s)
        result = " ".join(map(str, z[1:]))
        finish_time = datetime.datetime.now()
        result_time = (finish_time - start_time).total_seconds()
        print(f"Тест2. Время выполнения: {result_time} сек")

        # then
        self.assertEqual(result, expected_output)
        self.assertLessEqual(result_time, expected_time,
                            f"Время {result_time} сек превысило порог {expected_time} сек")

if __name__ == '__main__':
    unittest.main()