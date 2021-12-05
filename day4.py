import numpy as np
def main():
    with open("4_input.txt", "r") as f:
        order = list(map(int, f.readline().split(",")))
        board = list()
        for line in f:
            if line != '\n':
                board.append(list(map(int, filter(lambda x: x != '', line.split(' ')))))
        f.close()
        final_score = draw(order, board)
        print(final_score)

def draw(order, board):
    for nxt in order:
        for i in range(0, len(board), 5):
            for row in range(0, 5):
                for num in range(0, 5):
                    if board[i:i+5][row][num] == nxt:
                        board[i:i+5][row][num] = 'X'
        checked = check(board, nxt)
        if (isinstance(checked, int)):
            return checked
                

def check(board, current_draw):

    def calculate(current_board):
        sum = 0;
        for row in current_board:
            for n in row:
                if n != 'X':
                    sum += n
        return sum * current_draw
    
    for i in range(0, len(board), 5):
        numpy_board = np.array(board[i:i+5])
        current_board = board[i:i+5]
        transposed_current_board = numpy_board.T.tolist()
        
        for row in range(0, 5):
            if transposed_current_board[row][0] == 'X' and len(set(current_board[row])) == 1:
                return calculate(current_board)
        for col in range(0, 5):
            if transposed_current_board[col][0] == 'X' and len(set(transposed_current_board[col])) == 1:
                return calculate(current_board)

    

if __name__ == "__main__":
    main()
