board = [
    [0,0,0,0,4,0,0,0,0],
    [0,1,4,0,0,0,0,0,6],
    [0,0,2,9,0,3,0,0,0],
    [2,0,0,0,7,0,0,9,0],
    [0,9,0,0,0,0,5,0,0],
    [6,0,5,0,0,1,0,0,3],
    [5,0,0,0,0,0,7,2,0],
    [0,0,6,0,0,0,0,0,1],
    [0,0,0,0,0,7,0,3,0]
]

class Sudoku:

    def __init__(self, board):

        self.board = board

    def solveSudoku(self):
       
        position = self.emptySpace()
        if not position:
            self.showBoard()
            return True
        else:
            row, column = position

        invalid = self.validNumber(row, column)

        for i in range(1, 10):
            if i not in invalid:
                self.board[row][column] = i

                if self.solveSudoku():
                    return True
                self.board[row][column] = 0
                
        return False

    def emptySpace(self):
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if board[i][j] == 0 :
                    return (i, j) #Fila, columna
        return None

    def validNumber(self, row, col):
        # Arreglo de valores invalidos de uso
        numbers = []

        # Checar los numeros que ya estan en la misma fila
        for i in range(len(self.board)):
            if self.board[row][i] != 0:
                if self.board[row][i] not in numbers:
                    numbers.append(self.board[row][i])

        # Checar los numero que ya estan en la misma fila
        for j in range(len(self.board)):
            if self.board[j][col] != 0:
                if self.board[j][col] not in numbers:
                    numbers.append(self.board[j][col])

        # Checar en que cuadrado se encuentra
        box_x = col // 3
        box_y = row //3

        for i in range(box_y*3, box_y*3+3):
            for j in range(box_x*3, box_x*3+3):
                if self.board[i][j] != 0:
                    if self.board[i][j] not in numbers:
                        numbers.append(self.board[i][j])

        return numbers


    def showBoard(self):
        for i in range(len(self.board)):
            if i % 3 ==0 and i != 0:
                print('- - - - - - - - - -')
            for j in range(len(self.board)):
                if j % 3 == 0 and j != 0:
                    print('| ', end="")
                if j==8:
                    print(self.board[i][j])
                else:
                    print(str(self.board[i][j]) + ' ', end="")



if __name__ == "__main__":
    
    sudoku = Sudoku(board)
    sudoku.solveSudoku()