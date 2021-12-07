def solve(data):
    counter = 0
    for i in range(len(data) - 1):
        if data[i + 1] > data[i]:
            counter = counter + 1
    return counter


if __name__ == "__main__":
    data = []
    with open("input1.txt") as f:
        data = [int(i) for i in f.readlines()]
    
    print(solve(data))
