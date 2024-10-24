class Solution(object):
    def isValidSudoku(self, board):
        for i in range(9):
            array = [0] * 9
            array2 = [0] * 9
            for j in range(9):
                if(board[i][j]) != '.':
                    if array[int(board[i][j])-1] > 0:
                        #print("a")
                        return False
                    array[int(board[i][j])-1]+=1
                if(board[j][i]) != '.':
                    if array2[int(board[j][i])-1] > 0:
                        #print('b')
                        return False
                    array2[int(board[j][i])-1]+=1
        for box in range(9):
            row = (box // 3) * 3  
            col = (box % 3) * 3   
            array = [0] * 9      
            #print(row, col)
            for box2 in range(9):
                dX = box2 // 3    
                dY = box2 % 3    
                pos = row + dX    
                pos2 = col + dY   
                if (board[pos][pos2]) != '.':
                    if array[int(board[pos][pos2]) - 1] > 0:
                        #print('c')
                        return False
                    array[int(board[pos][pos2]) - 1] += 1
        return True

            