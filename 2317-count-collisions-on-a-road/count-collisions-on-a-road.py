class Solution:
    def countCollisions(self, directions: str) -> int:
        stack = []
        count = 0
        n = len(directions)
        for i in directions:
            if i=="L" and not stack:
                count += 1
            else :
                stack.append(i)
        stack = []
        sCount = 0 
        for i in directions[::-1]:
            print(i)
            if i=="S":
                sCount += 1
            if i=="R" and not stack:
                count += 1
            else :
                stack.append(i)
        return n-count-sCount

        


        