class Solution:
    def longestValidParentheses(self, S: str) -> int:
        openbracket=0
        closebracket=0
        max_length=0
        length=0
        for i in S:
            if i=="(":
                openbracket+=1
            if i==")":
                closebracket+=1
            if closebracket==openbracket:
                length=2*closebracket
            if closebracket>openbracket:
                closebracket=0
                openbracket=0
            max_length=max(length,max_length)
        openbracket=0
        closebracket=0
        n=len(S)
        length=0
        for i in range(n-1,-1,-1):
            if S[i]=="(":
                openbracket+=1
            if S[i]==")":
                closebracket+=1
            if closebracket==openbracket:
                length=2*closebracket
            if closebracket<openbracket:
                closebracket=0
                openbracket=0
            max_length=max(length,max_length)
        
        return max_length