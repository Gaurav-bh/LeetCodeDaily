class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        dic = {"X--":-1,"--X":-1,"X++":1,"++X":1}
        x = 0
        for op in operations:
            x += dic[op]
        return x

        