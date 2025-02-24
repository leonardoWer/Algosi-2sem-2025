"""
В файле собраны функции-удобства:
 - Чтение файла input.txt
 - Запись в файл output.txt
"""

import datetime
import tracemalloc
import os


INPUT_RELATIVE_PATH = "../txtfiles/input.txt"
OUTPUT_RELATIVE_PATH = "../txtfiles/output.txt"

# Функции для работы с файлами

def read_file(path:str = INPUT_RELATIVE_PATH):
    """
    Функция считывает данные с файла
     - Возвращает: (список строк с данными)
     - В файле где будет использоваться функция нужно определить путь:
     PATH = os.path.dirname(os.path.abspath(__file__))
    """
    file_path = os.path.join(path, INPUT_RELATIVE_PATH)
    result = []
    with open(file_path, "r", encoding="utf8") as file_input:
        for s in file_input:
            result.append(s.strip())

    return result

def str_to_list(text:str) -> list:
    """
    Принимает строку вида: "1 2 3 4 5 6 7 8"
    Возвращает список: [1,2,3,4,5,6,7,8]
    """
    return list(map(int, text.split()))

def write_file(path:str = OUTPUT_RELATIVE_PATH, data: list = None, repeat_el = False):
    """
    Функция записывает данные в файл
     - Принимает на вход список всех данных, которые нужно записать
     - Записывает данные в файл
    """
    file_path = os.path.join(path, OUTPUT_RELATIVE_PATH)
    file_out = open(file_path, "w", encoding="utf8")
    for el in data:
        if type(el) == list:
            res = " ".join([str(i) for i in el])  # Список с результатом приводим к строке и записываем в файл
            file_out.write(res)
            if len(data) > 1 and data[-1] == el and type(data[-1]) == list:
                file_out.write("\n")
        elif type(el) == int:
            file_out.write(str(el))
        elif type(el) == str:
            file_out.write(el)
        if len(data) > 1 and data[-1] != el:
            file_out.write("\n")
        elif len(data) > 1 and repeat_el:
            file_out.write("\n")

    file_out.close()


# Функции для тестов времени и памяти для разных функций

def test_memory_and_time_lst(lst: list, func, need_print:bool):
    """
    Выводит затрачиваемое время и память для сортировки
    - Формат входных данных вызова: (список, функция, нужно ли выводить результат)
    - Формат входных данных для функции (список)
    - Результат функции не выводит
    """
    print(f"Просчитаем время и память работы Сортировки {func}")
    tracemalloc.start()  # Запускаем счётчик памяти
    start_time = datetime.datetime.now()  # Запускаем счётчик времени

    func(lst)
    if need_print:
        if func(lst) is not None:
            print(func(lst))
        else:
            print(lst)

    finish_time = datetime.datetime.now()  # Измеряем время конца работы
    print("Итоговое время:", finish_time - start_time)  # Выводим итоговое время

    current, peak = tracemalloc.get_traced_memory()  # Присваеваем двум переменным память, используемую сейчас, и на пике
    print(
        f"Используемая память: {current / 10 ** 6} МБ\nПамять на пике: {peak / 10 ** 6} МБ\n")  # Выводим время работы в мегабайтах


def test_memory_and_time_lst_n(lst: list, n: int, func, need_print:bool):
    """
    Выводит затрачиваемое время и память для сортировки
    - Формат входных данных вызова: (список, количество элементов, функция, нужно ли выводить результат)
    - Формат входных данных для функции (список, левый, правый)
    - Результат функции не выводит
    """
    print(f"Просчитаем время и память работы Сортировки {func}")
    tracemalloc.start()  # Запускаем счётчик памяти
    start_time = datetime.datetime.now()  # Запускаем счётчик времени

    func(lst, 0, n - 1)
    if need_print:
        if func(lst, 0, n - 1) is not None:
            print(func(lst, 0, n - 1))
        else:
            print(lst)

    finish_time = datetime.datetime.now()  # Измеряем время конца работы
    print("Итоговое время:", finish_time - start_time)  # Выводим итоговое время

    current, peak = tracemalloc.get_traced_memory()  # Присваеваем двум переменным память, используемую сейчас, и на пике
    print(
        f"Используемая память: {current / 10 ** 6} МБ\nПамять на пике: {peak / 10 ** 6} МБ\n")  # Выводим время работы в мегабайтах
