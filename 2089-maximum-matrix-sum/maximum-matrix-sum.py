class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        su = 0
        neg = []
        flag = False
        negCount = 0
        for i in range(n):
            for j in range(n):
                if matrix[i][j] <0:
                    negCount += 1
                   
                if matrix[i][j]==0:
                    flag = True
                neg.append(abs(matrix[i][j]))
                su += abs(matrix[i][j])
        if flag:
            return su
        if negCount%2==1:
            neg.sort()
            print(neg[0])
            print(su)
            su -= 2*neg[0]
        return su
        