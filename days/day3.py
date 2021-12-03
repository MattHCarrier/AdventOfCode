import math


def find_common(binary: list):
    positions = {0: {0: 0, 1: 0},
                 1: {0: 0, 1: 0},
                 2: {0: 0, 1: 0},
                 3: {0: 0, 1: 0},
                 4: {0: 0, 1: 0},
                 5: {0: 0, 1: 0},
                 6: {0: 0, 1: 0},
                 7: {0: 0, 1: 0},
                 8: {0: 0, 1: 0},
                 9: {0: 0, 1: 0},
                 10: {0: 0, 1: 0},
                 11: {0: 0, 1: 0}}

    for d in binary:
        for i, b in enumerate(d):
            positions[i][int(b)] += 1
    return positions


def day3_problem_one(data: list):
    def convert_decimal(binary):
        decimal = 0
        counter = 0
        for i in range(len(binary) - 1, 0, -1):
            decimal += int(binary[counter]) * math.pow(2, i)
            counter += 1
        return decimal
    positions = find_common(data)
    gamma = ""
    epsilon = ""
    for position in positions.values():
        max = "0" if position[0] > position[1] else "1"
        min = "1" if position[0] > position[1] else "0"
        gamma += max
        epsilon += min
    gamma_decimal = convert_decimal(gamma)
    epsilon_decimal = convert_decimal(epsilon)

    return gamma_decimal * epsilon_decimal


def day3_problem_two(data: list):
    pass
