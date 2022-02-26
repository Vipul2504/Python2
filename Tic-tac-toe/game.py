class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.currentwinner = None
        
    def printboard(self):
        for row in [self.board[i*3:(i+1)*3] for in range(3)]:
            print(' | ' + ' | '.join(row) + ' | ')
            
    @staticmethod
    def printboard_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print(' | ' + ' | '.join(row) + ' | ')