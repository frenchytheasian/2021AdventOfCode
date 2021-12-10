from pprint import pprint

def parse_data():
    with open("day4.txt", "r") as file:
        contents = file.read()
        sections = contents.split("\n\n")
        numbers = [int(num) for num in sections[0].split(",")]
        boards_raw = sections[1:]
        boards = []
        for board_raw in boards_raw:
            rows_raw = board_raw.split("\n")
            board = []
            for row_raw in rows_raw:
                row = [int(num) for num in row_raw.split()]
                board.append(row)
            boards.append(board)
    return (numbers, boards)

def check_rows(board):
    for i, row in enumerate(board):
        if len([num for num in row if (num == None or num < 0)]) == 5:
            return i
    return False

def check_columns(board):
    for i in range(len(board[0])):
        if len([row[i] for row in board if (row[i] == None or row[i] < 0)]) == 5:
            return i
    return False

def check_win(board):
    row = check_rows(board)
    col = check_columns(board)
    if type(row) != bool:
        return ("R", row)
    elif type(col) != bool:
        return ("C", col)
    else:
        return False

def play_bingo(numbers, boards):
    result = None

    while numbers:
        current_number = numbers.pop(0)
        for i, board in enumerate(boards):
            for j, row in enumerate(board):
                for k, num in enumerate(row):
                    if num == current_number:
                        boards[i][j][k] *= -1
                        if num == 0:
                            boards[i][j][k] = None
        
        for l, board in enumerate(boards):
            result = check_win(board)
            if result and len(boards) != 1:
                boards.remove(board)
                result = None
        if len(boards) == 1:
            if result:
                return (boards[0], current_number)
    print(len(boards))


def calculate_score(board, number):
    unchecked_sum = 0
    for row in board:
        for i in row:
            if i != None and i > 0:
                unchecked_sum += i
    return unchecked_sum*number
    
def main():
    data = parse_data()
    numbers = data[0]
    boards = data[1]
    data = play_bingo(numbers, boards)
    score = calculate_score(data[0], data[1])
    print(score)
    

        

    

if __name__ == "__main__":
    main()