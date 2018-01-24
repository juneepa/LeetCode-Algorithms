## https://leetcode.com/problems/toeplitz-matrix/description/
## A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.
## Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
## Easy, 93ms, Not Enough Data

class Solution:
    def isToeplitzMatrix(self, matrix):
        
        for i in range(len(matrix) - 1):
            ## Check row[:-1] == next_row[1:]
            ## Toeplitz Matrix must satisfy the condition above since every diagonal from t-l to b-r has the same element
            if matrix[i][:-1] != matrix[i + 1][1:]:
                return False
        
        return True
        
        
        
        
        
        
