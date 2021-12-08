def solve(data):
    data2 = data.copy()
    size = int(len(data[0]))
    oxygen = ''

    for i in range(size):
        zero_count = 0
        one_count = 0
        for j in range(len(data)):
            if data[j][i] == '0':
                zero_count += 1
            if data[j][i] == '1':
                one_count += 1

        if zero_count > one_count:
            oxygen = '0'
        else:
            oxygen = '1'

        if len(data) > 1:
            data_copy = []
            for j in range(len(data)):
                if data[j][i] == oxygen:
                    data_copy.append(data[j])
            data = data_copy

        zero_count = 0
        one_count = 0
        for j in range(len(data2)):
            if data2[j][i] == '0':
                zero_count += 1
            if data2[j][i] == '1':
                one_count += 1

        if zero_count > one_count:
            oxygen = '1'
        else:
            oxygen = '0'

        if len(data2) > 1:
            data2_copy = []
            for j in range(len(data2)):
                if data2[j][i] == oxygen:
                    data2_copy.append(data2[j])
            data2 = data2_copy

    return int(data[0], base=2) * int(data2[0], base=2)


if __name__ == "__main__":
    data = []
    with open("input2.txt") as f:
        data = [i.strip() for i in f.readlines()]
    
    print(solve(data))
