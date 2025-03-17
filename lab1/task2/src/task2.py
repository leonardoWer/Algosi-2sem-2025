from utils import utils
import os


PATH = os.path.dirname(os.path.abspath(__file__))


def min_refills(d, m, stops):
    stops = [0] + stops + [d]  # Добавляем стартовую и конечную точки
    num_refills = 0
    current_position = 0  # Текущая заправка (индекс)

    while current_position < len(stops) - 1:
        last_position = current_position

        # Пока можем доехать до следующей заправки, едем дальше
        while (current_position < len(stops) - 1 and
               stops[current_position + 1] - stops[last_position] <= m):
            current_position += 1

        # Если мы не сдвинулись, то заправок не хватает
        if current_position == last_position:
            return -1

        # Если не доехали конца, считаем заправку
        if current_position < len(stops) - 1:
            num_refills += 1

    return num_refills


if __name__ == "__main__":
    lst = utils.read_file(PATH)
    d = int(lst[0])
    m = int(lst[1])
    n = int(lst[2])
    stops = utils.str_to_list(lst[3])
    result = min_refills(d, m, stops)

    utils.write_file(PATH, [result])