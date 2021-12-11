def get_score(board, marked_nums):
    board_nums = []
    for row in board:
        for cell in row:
            board_nums.append(cell)
    unmarked_nums = set(board_nums) - set(marked_nums)
    return sum(unmarked_nums)


def check(board, marked_nums):
    cols = []
    for j in zip(*board):
        cols.append(list(j))
    lines = board + cols
    for line in lines:
        if all([cell in marked_nums for cell in line]):
            return True
    return False


def solve(boards, nums):
    marked_nums = []
    board_list = []
    solves = []

    for num in nums:
        marked_nums.append(num)
        for i, board in enumerate(boards):
            if check(board, marked_nums):
                if i not in board_list:
                    board_list.append(i)
                    solves.append((get_score(board, marked_nums), num))
    return solves


if __name__ == "__main__":
    data = []
    with open("input.txt") as f:
        data = [i.strip() for i in f.readlines()]

    nums = []
    for i in data[0].split(","):
        nums.append(int(i))

    del data[0:2]

    boards = []
    j = 0
    while j + 5 <= len(data):
        board = []
        for row in data[j:j+5]:
            cells = []
            for cell in row.split():
                cells.append(int(cell))
            board.append(cells)
        boards.append(board)
        j = j + 6
    
    forward, reverse = solve(boards, nums)[0], solve(boards, nums)[-1]
    part1 = forward[0] * forward[1]
    part2 = reverse[0] * reverse[1]
    print(part1)
    print(part2)
