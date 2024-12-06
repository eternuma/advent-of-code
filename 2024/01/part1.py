def solve(data):


if __name__ == "__main__":
    data = []
    with open("input1.txt") as f:
        data = [int(i) for i in f.readlines()]
    
    print(solve(data))
