from days.day1 import problem_one


def read_data(path):
    with open(path) as file:
        data = [int(line.strip()) for line in file]
    return data


if __name__ == '__main__':
    day_one_data = read_data(".\data\day1.txt")
    SOLUTION_ONE = problem_one(day_one_data)
    print(SOLUTION_ONE)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
