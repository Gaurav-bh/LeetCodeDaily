class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        
        
        # Function to find all substrings
        def find_substrings(s):
            res = set()
            for i in range(len(s)):
                for j in range(i, len(s)+1):
                    res.add(s[i:j])
            return list(res)
        s_set=find_substrings(s)
        t_set=find_substrings(t)
        max_long=0
        for i in s_set:
            for j in t_set:
                #print(longestPalindrome(i+j))
                word=i+j
                if word==word[::-1]:
                    max_long=max(max_long,len(word))

        return max_long
        

        
        
