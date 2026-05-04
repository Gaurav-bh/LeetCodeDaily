import bisect
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        sSize = len(s)
        charDic = {}
        for i in range(sSize):
            char = s[i]
            if char not in charDic:
                charDic[char] = []

            charDic[char].append(i)



        def check(word):
            prev = -1

            for char in word:
                if char not in charDic:
                    return False
                listCharInd = charDic[char]
                listSize = len(listCharInd)
                curr = ""
                if listSize==1:
                    curr = listCharInd[0]
                else:
                    ind = bisect.bisect_right(listCharInd,prev)
                    if ind == listSize:
                        return False
                    curr = listCharInd[ind]
                
                if curr <= prev:
                    return False

                prev = curr
            return True

        print(charDic)
        countSub = 0
        for word in words:
            if check(word):
                print(word)
                countSub +=1
        return countSub
    # wpddkvbnn

# {'r': [0, 71, 77, 82, 86], 'w': [1, 24, 28, 37, 43, 81], 'p': [2, 62], 'd': [3, 4, 42, 47, 67, 87], 'k': [5, 21, 36, 41, 66, 79, 93], 'v': [6, 17, 34, 50, 70, 73], 'b': [7, 29, 33, 53, 75, 85], 'n': [8, 9, 13, 61, 84, 91], 'u': [10, 39, 46, 52, 72], 'g': [11, 15, 27, 31, 35, 55], 'l': [12, 56, 65], 'a': [14, 18, 74, 92, 98], 't': [16, 23, 95], 'm': [19], 'x': [20, 49], 'q': [22, 26, 30, 40, 64, 69, 96], 'h': [25, 44], 'f': [32, 60, 80], 'y': [38, 88, 89], 'z': [45], 's': [48, 68, 94], 'j': [51, 54, 63, 76, 90, 97], 'o': [57, 59, 83], 'e': [58], 'i': [78], 'c': [99]

# 1 2 3



    #     bb is possible to be made by s="abcde"
    #     dic {a:0, b:1, c:4,d:6,e:(2,5)}
    #     abcde
    #     dic 

    #     ace
    #     0,2,4

    #     list = a : - [0]
    #     len==1:
    #     if len>1:
    #         leftbisect in list()

    #     3
    #     e = (2,5)
    #     l = len(e)
    #     if index<l:
    #         curr = e[]

    #     s = aebcde
    #     ace
    #     dic {a:[0]], b:2, c:3,d:4,e:(1,5)} 

    # for char in word
    #    ace
    #    prev = -1
    #    take out list from dic[a] = l = [0]
    #    if len(l) ==1
    #     curr = l[0]

        
    #     ace l = [1,5]
    #     prev = 3
    #     elif len(l)>1:
    #         ind = leftbisec(l,prev)#1
    #         if ind==len(l):
    #             return False

    #         curr = l[ind]
            

    #     curr <prev return False

    #     prev = curr

    




    #     prev = curr

    # return True


    #     check(i,j)
    #     if j == len(n):
    #         return True
    #     flag = False
    #     if s[i] - word[j]:
    #         check(i+1,j+1)

    #     check (i+1,j)

    #     Time :- O(len(words) *(len(s)+max(len(word)) )


    #     Time:- O(len(words)) *(max(len(word)*max(log(s)))) + len(s) #dic creation