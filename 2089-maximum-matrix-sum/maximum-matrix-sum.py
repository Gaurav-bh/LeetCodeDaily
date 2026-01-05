class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        su = 0
        minValue = 99999999
        flag = False
        negCount = 0
        for i in range(n):
            for j in range(n):
                if matrix[i][j] <0:
                    negCount += 1
                   
                if matrix[i][j]==0:
                    flag = True
                minValue = min(minValue,abs(matrix[i][j]))
                su += abs(matrix[i][j])
        if flag:
            return su
        if negCount%2==1:
            
            su -= 2*minValue
        return su
        