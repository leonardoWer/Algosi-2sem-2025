from utils import utils
import os

PATH = os.path.dirname(os.path.abspath(__file__))


def find_shortest_distance(reactions: list, start_substance: str, target_substance: str) -> int:
    """
    Находит кратчайшее количество реакций для получения целевого вещества из исходного.

    Args:
        reactions: Список алхимических реакций, где каждый элемент - кортеж (исходное вещество, целевое вещество).
        start_substance: Исходное вещество.
        target_substance: Целевое вещество.

    Returns:
        Минимальное количество реакций или -1, если целевое вещество недостижимо.
    """

    # Граф, в котором узлами будут элементы
    graph = {}
    for reaction in reactions:
        initial_substance, final_substance = reaction[0], reaction[1]
        # Если нет исходного вещества
        if initial_substance not in graph:
            graph[initial_substance] = []

        # Добавляем результат
        graph[initial_substance].append(final_substance)

    # Находим кратчайший путь от начала до цели
    queue = [(start_substance, 0)]  # (вещество, расстояние)
    visited = {start_substance}

    while queue:
        current_substance, distance = queue.pop(0)

        if current_substance == target_substance:
            return distance

        if current_substance in graph:
            for next_substance in graph[current_substance]:
                if next_substance not in visited:
                    queue.append((next_substance, distance + 1))
                    visited.add(next_substance)
    return -1


def format_reactions(reactions_list: list) -> list:
    """Форматируем реакции из стрелочного формата в списочный"""
    formatted_reactions = []
    for reaction in reactions_list:
        formatted_reactions.append(list(reaction.split(" -> ")))

    return formatted_reactions


def main() -> list:
    """
    Выведите минимальное количество алхимических реакций,
    которое требуется для получения требуемого вещества из исходного,
    или -1, если требуемое вещество невозможно получить
    """
    lst = utils.read_file(PATH)
    m = int(lst[0])
    reactions = format_reactions(lst[1:m + 1])
    start_substance = lst[m + 1]
    target_substance = lst[m + 2]
    return [find_shortest_distance(reactions, start_substance, target_substance)]


if __name__ == "__main__":
    result = main()
    utils.write_file(PATH, result)
