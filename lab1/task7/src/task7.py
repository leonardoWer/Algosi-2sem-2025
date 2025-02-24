from utils import utils
import os


PATH = os.path.dirname(os.path.abspath(__file__))


def shoemaker_problem(k:int, n:int, t:list) -> int:
    cnt = 0
    summ = 0
    # Если время первой пары сапог > рабочий день, то рабочий сделает 0 пар
    if t[0] > k:
        cnt = 0
    else:
        for i in range(n):
            while summ <= k:
                summ += t[i]
                cnt += 1
    return cnt


if __name__ == "__main__":
    lst = utils.read_file(PATH)
    k, n = utils.str_to_list(lst[0])
    t = utils.str_to_list(lst[1])
    k1, n1 = utils.str_to_list(lst[2])
    t1 = utils.str_to_list(lst[3])
    result = shoemaker_problem(k, n, t)
    result1 = shoemaker_problem(k1, n1, t1)
    utils.write_file(PATH, [result, result1])