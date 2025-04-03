from utils import utils
import os

PATH = os.path.dirname(os.path.abspath(__file__))


def solve():
    # Чтение входных данных из файла
    lst = utils.read_file(PATH)

    p = lst[0]  # Подстрока p
    t = lst[1]  # Строка t

    len_p = len(p)
    len_t = len(t)

    # Список для хранения индексов начала вхождений
    result_indices = []

    # Наивный поиск всех вхождений подстроки p в строку t
    for i in range(len_t - len_p + 1):
        if t[i:i + len_p] == p:
            result_indices.append(i + 1)  # Индексы начинаются с 1

    # Количество вхождений
    count = len(result_indices)

    # Запись результатов в файл
    utils.write_file(PATH, [[count], result_indices], True)


if __name__ == "__main__":
    solve()
