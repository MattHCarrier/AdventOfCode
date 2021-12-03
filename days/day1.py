
def day1_problem_one(data: list):
    increases = 0

    for i in range(1, len(data)):
        if data[i - 1] < data[i]:
            increases += 1
    return increases


def day1_problem_two(data: list):
    increases = 0
    for i in range(3, len(data)):
        window_one = data[i - 3] + data[i - 2] + data[i - 1]
        window_two = data[i - 2] + data[i - 1] + data[i]
        if window_two > window_one:
            increases += 1
    return increases
