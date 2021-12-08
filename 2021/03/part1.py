def solve(data):
    gamma = 0
    epsilon = 0
    size = int(len(data[0]))
    binsplit = zip(*data)

    gamma_str = ""
    for i in binsplit:
        if i.count("1") > i.count("0"):
            gamma_str += "1"
        else:
            gamma_str += "0"
    print(gamma_str)
    gamma = int(gamma_str, base=2)

    epsilon = (2 ** size) - gamma - 1
    return gamma * epsilon


if __name__ == "__main__":
    data = []
    with open("input1.txt") as f:
        data = [i.strip() for i in f.readlines()]
    
    print(solve(data))
