import unittest
import datetime
from itertools import product
from utils import utils
from lab1.task22.src.task22 import count_beautiful_patterns
import os


class TestCountInversion(unittest.TestCase):
    print("Lab1 task22 test")
    def test_1(self):
        # given
        m, n = 2, 2
        expect_result = 14
        expected_time = 4

        # when
        start_time = datetime.datetime.now()
        result = count_beautiful_patterns(m, n)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест1.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_2(self):
        # given
        m, n = 3, 3
        expect_result = 322
        expected_time = 4

        # when
        start_time = datetime.datetime.now()
        result = count_beautiful_patterns(m, n)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест2.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")

    def test_3(self):
        # given
        m, n = 1, 1
        expect_result = 2
        expected_time = 4

        # when
        start_time = datetime.datetime.now()
        result = count_beautiful_patterns(m, n)
        finish_time = datetime.datetime.now()
        result_time = finish_time - start_time
        print("Тест2.Итоговое время алгоритма:", result_time)

        # then
        self.assertEqual(result, expect_result)
        self.assertLessEqual(result_time.total_seconds(), expected_time, f"Значение {result_time} превышает порог {expected_time}")


if __name__ == '__main__':
    unittest.main()