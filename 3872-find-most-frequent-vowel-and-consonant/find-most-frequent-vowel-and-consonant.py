class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel = SortedDict()
        consoment = SortedDict()
        vowelList = set("AEIOUaeiou")
        print(vowelList)
        vowelMax = 0
        conMax = 0

        for char in s:
            if char in vowelList:
                if char not in vowel:
                    vowel[char] = 0
                vowel[char] +=1
                vowelMax = max(vowelMax,vowel[char])

            else:
                if char not in consoment:
                    consoment[char] = 0
                consoment[char] +=1
                conMax = max(conMax,consoment[char])
        
        return conMax + vowelMax


        