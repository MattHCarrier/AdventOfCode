from aocd import get_data
from aocd import submit


def problem_one(data: list):
    increases = 0
    for i in range(1, len(data)):
        if data[i-1] < data[i]:
            increases += 1
    return increases


