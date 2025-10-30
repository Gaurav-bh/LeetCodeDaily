class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        count = target[0]
        n = len(target)
        prev = target[0]
        for i in range(1,n):

            if target[i]<=prev:
                prev = target[i]
            else:
                count += target[i] - prev
                prev =  target[i]
        return count
        