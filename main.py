from days.day1 import (day1_problem_one, day1_problem_two)
from days.day2 import (day2_problem_one, day2_problem_two)
from days.day3 import (day3_problem_one, day3_problem_two)


def read_data(path, list_type):
    with open(path) as file:
        if list_type == "int":
            data = [int(line.strip('\n')) for line in file]
        else:
            data = [line.strip('\n') for line in file]
    return data


def day1_solutions():
    """
    solutions to day one advent of code
    :return:
    """
    day_one_data = read_data(".\data\day1.txt", "int")
    SOLUTION_ONE = day1_problem_one(day_one_data)
    print(SOLUTION_ONE)
    SOLUTION_TWO = day1_problem_two(day_one_data)
    print(SOLUTION_TWO)


def day2_solutions():
    day_two_data = read_data(".\data\day2.txt", "str")
    SOLUTION_ONE = day2_problem_one(day_two_data)
    print(SOLUTION_ONE)
    SOLUTION_TWO = day2_problem_two(day_two_data)
    print(SOLUTION_TWO)

def day3_solutions():
    day_three_data = read_data(".\data\day3.txt", "str")
    SOLUTION_ONE = day3_problem_one(day_three_data)
    print(SOLUTION_ONE)


if __name__ == '__main__':
    # day1_solutions()
    # day2_solutions()
    day3_solutions()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
