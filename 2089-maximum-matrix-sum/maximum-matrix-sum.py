class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        su = 0
        minValue = 999999
    
        negCount = 0
        for i in range(n):
            for j in range(n):
                if matrix[i][j] <0:
                    negCount += 1
                minValue = min(minValue,abs(matrix[i][j]))
                su += abs(matrix[i][j])
        
        if negCount%2==1:
            
            su -= 2*minValue
        return su
        