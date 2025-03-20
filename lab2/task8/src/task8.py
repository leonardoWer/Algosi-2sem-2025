from utils import utils
import os

PATH = os.path.dirname(os.path.abspath(__file__))


def find_tree_height(tree, root):
    """Рекурсивный поиск высоты дерева"""
    if root == 0:  # если узел отсутствует то высота дерева = 0
        return 0
    # в обратном случае находим высоту поддеревьев и возвращаем максимум + 1 (корень)
    left = tree[root][1]
    right = tree[root][2]
    return 1 + max(find_tree_height(tree, left), find_tree_height(tree, right))


def main():
    # Читаем данные из файла
    lst = utils.read_file(PATH)  # строки
    N = int(lst[0])  # количество вершин

    if N == 0:
        utils.write_file(PATH, ["0"])
        return

    # строим дерево

    tree = {}
    children = set()  # дочерние узлы

    for i in range(1, N + 1):
        key, left, right = map(int, lst[i].split())  # узел и потомки
        tree[i] = (key, left, right)
        if left > 0:
            children.add(left)
        if right > 0:
            children.add(right)

    # Определяем корень, вычитая все дочерние узлы, оставляя только корень
    root = (set(range(1, N + 1)) - children).pop()

    # Вычисляем высоту дерева
    height = find_tree_height(tree, root)

    # Записываем результат в файл
    utils.write_file(PATH, [str(height)])


if __name__ == "__main__":
    main()
