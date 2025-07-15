class Solution:
    def isValid(self, word: str) -> bool:
        Vowels= ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        Consonants= ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v','w', 'x', 'y', 'z','B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N','P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
        vowel_count=0
        consonent_count=0
        for char in word:
            if char in Vowels:
                vowel_count+=1
            if char in Consonants:
                consonent_count+=1
        if len(word)>=3 and word.isalnum() and vowel_count and consonent_count:
            return True
        return False


        