def solve(data):
    horizontal = 0
    depth = 0
    aim = 0
    for val in data:
        direction = val.strip().split()[0]
        num = int(val.strip().split()[1])
        if direction == "up":
            aim = aim - num
        elif direction == "down":
            aim = aim + num
        else:
            horizontal = horizontal + num
            depth = depth + (aim * num)
    return horizontal * depth


if __name__ == "__main__":
    data = []
    with open("input1.txt") as f:
        data = [i for i in f.readlines()]
    
    print(solve(data))
