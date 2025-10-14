class Solution:
    def reverseVowels(self, s: str) -> str:
        vowelStack = []
        vowel = ('a','e','i','o','u','A','E','I','O','U')
        for i in s:
            if i in vowel :
                vowelStack.append(i)
        ans = ""
        for i in s:
            if i in vowel:
                ans += vowelStack.pop()
            else:
                ans += i
        return ans
        