def solve(data):
    counter = 0
    for i in range(len(data) - 3):
        if data[i + 1] + data[i + 2] + data[i + 3] > data[i] + data[i + 1] + data[i + 2]:
            counter = counter + 1
    return counter


if __name__ == "__main__":
    data = []
    with open("input2.txt") as f:
        data = [int(i) for i in f.readlines()]
    
    print(solve(data))
