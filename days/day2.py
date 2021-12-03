
def day2_problem_one(data: list):
    position = {"position": 0, "depth": 0}
    for command in data:
        instruction = command.split()
        if instruction[0] == "forward":
            position["position"] += int(instruction[1])
        if instruction[0] == "up":
            position["depth"] -= int(instruction[1])
        if instruction[0] == "down":
            position["depth"] += int(instruction[1])
    return position["position"] * position["depth"]


def day2_problem_two(data:list):
    position = {"position": 0, "depth": 0, "aim": 0}
    for command in data:
        instruction = command.split()
        if instruction[0] == "forward":
            position["position"] += int(instruction[1])
            position["depth"] += int(instruction[1]) * position["aim"]
        if instruction[0] == "up":
            position["aim"] -= int(instruction[1])
        if instruction[0] == "down":
            position["aim"] += int(instruction[1])
    return position["position"] * position["depth"]