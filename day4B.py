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
    def check(current_draw):
        def calculate():
            sum = 0;
            for row in board:
                for n in row:
                    if n != 'X':
                        sum += n
            return sum * current_draw

       
        complete_game = 0
        for i in range(len(board) - 5, -1, -5):
            if complete_game == 1:
                break
            complete_game = 0
            numpy_board = np.array(board[i:i+5])
            current_board = board[i:i+5]
            transposed_current_board = numpy_board.T.tolist()
            flag = 0
            for row in range(0, 5):
                if current_board[row][0] == 'X' and len(set(current_board[row])) == 1:
                    complete_game = 1 if len(board) == 5 else 0
                    if complete_game == 1:
                        flag = 1
                        break
                    del board[i:i+5]
                    flag = 1
                    break
            if flag == 1:
                continue
            for col in range(0, 5):
                if transposed_current_board[col][0] == 'X' and len(set(transposed_current_board[col])) == 1:
                    complete_game = 1 if len(board) == 5 else 0
                    if complete_game == 1:
                        flag = 1
                        break
                    del board[i:i+5]
                
        if complete_game == 1:
            return calculate()
                
    for nxt in order:
        for i in range(len(board) - 5, -1, -5):
            for row in range(0, 5):
                for num in range(0, 5):
                    if board[i:i+5][row][num] == nxt:
                        board[i:i+5][row][num] = 'X'
        checked = check(nxt)
        if (isinstance(checked, int)):
            return checked
                

    
    

if __name__ == "__main__":
    main()
