class KnightTour:

    def __init__(self, boardSize):
        self.boardSize = boardSize
        self.xMoves = [1, 2, 2, 1, -1, -2, -2, -1]
        self.yMoves = [2, 1, -1, -2, -2, -1, 1, 2]
        self.solutionMatrix = [[-1 for i in range(boardSize)] for j in range(boardSize)]

    def solveKnightTour(self):
        
        self.solutionMatrix[0][0] = 0

        if self.solveProblem(1, 0, 0):
            self.showSolution()
        else:
            print("There is no solution to this problem...")

    def solveProblem(self, stepCount, x, y):
        
        if stepCount == self.boardSize**2:
            return True
        
        for i in range(self.boardSize):

            nextX = x + self.xMoves[i]
            nextY = y + self.yMoves[i]

            if self.isValidPlace(nextX, nextY):

                self.solutionMatrix[nextX][nextY] = stepCount
                
                if self.solveProblem(stepCount+1, nextX, nextY):
                    return True
                
                self.solutionMatrix[nextX][nextY] = -1
                
        return False
        

    def isValidPlace(self, x, y):

        if x < 0 or x >= self.boardSize:
            return False

        if y < 0 or y >= self.boardSize:
            return False

        if self.solutionMatrix[x][y] > -1:
            return False

        return True

    def showSolution(self):
	
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                print(self.solutionMatrix[i][j],end=" "),
                
            print('\n')
        print('\n')

    
if __name__ == "__main__":
    knight = KnightTour(7)
    knight.solveKnightTour()