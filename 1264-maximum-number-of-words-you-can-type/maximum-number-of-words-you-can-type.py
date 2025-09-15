class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        letterSet=set()
        for i in brokenLetters:
            letterSet.add(i)
        words=text.split(" ")
        count=0
        for word in words:
            for letter in letterSet:
                if letter in word:
                    break
            else:
                count+=1
        return count
        
        