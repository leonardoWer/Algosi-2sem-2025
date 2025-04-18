"""
Напишите программу, реализующую структуру данных, позволяющую добавлять и удалять элементы
а также находить k-й максимум
"""

from utils import utils
import os

PATH = os.path.dirname(os.path.abspath(__file__))


class KMax:
    data = []  # Список для хранения данных
    output_data = []  # Список для хранения выходных данных(при вводе команды 0)

    def handle_list_input_data(self, commands_cnt: int, commands_list: list) -> list:
        """Переводит список команд в удобный вид"""
        handled_commands_list = []
        for i in range(commands_cnt):
            command_name, command_index = map(int, commands_list[i].split())
            handled_commands_list.append([command_name, command_index])

        return handled_commands_list

    def handle_commands_list(self, commands_cnt: int, commands_list: list):
        """Обрабатывает команды, поданные на вход в списке"""
        handled_commands_list = self.handle_list_input_data(commands_cnt, commands_list)
        for operation in handled_commands_list:
            command, key = operation[0], operation[1]
            if command > 0:
                self.add_el_with_k_key(key)
            elif command < 0:
                self.remove_el_with_k_key(key)
            else:
                self.find_and_get_k_max(key)

    def add_el_with_k_key(self, key):
        self.data.append(key)

    def find_and_get_k_max(self, key):
        if not self.data:
            raise IndexError

        sorted_data = sorted(self.data, reverse=True)  # Ключевой шаг, сортируем элементы по убыванию в новый список
        if key <= len(sorted_data):
            """
            Извлечение k-го максимума. Поскольку нумерация элементов в списке начинается с 0, 
            а key обозначает порядковый номер (начиная с 1), для доступа к нужному элементу используется индекс key - 1. 
            Найденный k-й максимум добавляется в список выходных данных.
            """
            self.output_data.append(sorted_data[key - 1])

    def remove_el_with_k_key(self, key):
        try:
            self.data.remove(key)
        except ValueError:
            pass  # Игнорируем, если элемента нет (по условию гарантируется, что его не будет)

    def get_output_data(self):
        return self.output_data


def main():
    lst = utils.read_file(PATH)
    commands_cnt = int(lst[0])
    commands_list = lst[1:]
    kmax = KMax()
    kmax.handle_commands_list(commands_cnt, commands_list)
    return kmax.get_output_data()


if __name__ == "__main__":
    result = main()
    utils.write_file(PATH, result, True)
