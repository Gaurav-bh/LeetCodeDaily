class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        stack = []
        count = 0
        for i,val in enumerate(colors):
            curr = val
            k = i
            #print(curr,k)
            #print(stack,count)
            if stack and stack[-1][1]==curr:
                stackTop = stack.pop()
                prev = stackTop[0]
                prevVal = stackTop[1]
                if neededTime[prev]> neededTime[k]:
                    count += neededTime[k] 
                    curr = prevVal
                    k = prev
                else:
                    count += neededTime[prev] 
                   
            stack.append((k,curr))
        print(stack)
        return count

                    
        