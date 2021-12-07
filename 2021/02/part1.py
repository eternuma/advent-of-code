def solve(data):
    horizontal = 0
    depth = 0
    for val in data:
        direction = val.strip().split()[0]
        num = int(val.strip().split()[1])
        if direction == "up":
            depth = depth - num
        elif direction == "down":
            depth = depth + num
        else:
            horizontal = horizontal + num
    return horizontal * depth


if __name__ == "__main__":
    data = []
    with open("input1.txt") as f:
        data = [i for i in f.readlines()]
    
    print(solve(data))
