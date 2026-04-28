
class Solution:
    def checkValidString(self, s: str) -> bool:

        n = len(s)

        cache = dict()

        min_open = 0 
        max_open = 0 

        for i in range(n):
            

            if s[i] == "(":
                min_open += 1 
                max_open += 1

            elif s[i] == ")":
                min_open -= 1 
                max_open -= 1

            else:
                min_open -= 1
                max_open += 1

            if min_open < 0 :
                min_open = 0 

            if max_open < 0 :
                return False

        return min_open == 0   
        