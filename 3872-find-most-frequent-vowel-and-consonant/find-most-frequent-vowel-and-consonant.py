class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel = SortedDict()
        consoment = SortedDict()
        vowelList = set("AEIOUaeiou")
        print(vowelList)

        for char in s:
            if char in vowelList:
                if char not in vowel:
                    vowel[char] = 0
                vowel[char] +=1
            else:
                if char not in consoment:
                    consoment[char] = 0
                consoment[char] +=1
        vowelMax = 0
        conMax = 0
        for i in vowel:
            vowelMax = max(vowelMax,vowel[i])
        
        for i in consoment:
            conMax = max(conMax,consoment[i])
        return conMax + vowelMax


        