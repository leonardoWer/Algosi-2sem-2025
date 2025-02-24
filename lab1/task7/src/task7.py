from utils import utils
import os


PATH = os.path.dirname(os.path.abspath(__file__))


if __name__ == "__main__":
    lst = utils.read_file(PATH)
    k, n = lst[0].split()
    t = utils.str_to_list(lst[1])