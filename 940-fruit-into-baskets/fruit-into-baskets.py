"""
input:- 
list fruits type =[1,2,1]

output:- 
count of fruits we can take :- 3


approach 1 : nrute force 
 check all the window of any size which contains only two type of fruits 

time :- O(N*N*N)
N*N for differet size windows and N for checking the two types of fruits only 
space :- O(1)


Approach 2 :- 
    as window problem we can use the sliding window to get the window on some condition 
        condition :- if window size has only 2 type inc else dec the size 
            to check the two types of fruits we can dic for each type and keep check the size 


    Time :- O(N)
    Space :- O(F (Type for fruits))

"""
class Solution:

    def totalFruit(self, fruits: List[int]) -> int:
        size=len(fruits)
        leftPtr=0
        fruitHash={}
        maxLength=0
        for i in range(size):
            if fruits[i] in fruitHash:
                fruitHash[fruits[i]]+=1
            else:
                fruitHash[fruits[i]]=1

            while len(fruitHash)>2:
                if fruitHash[fruits[leftPtr]]==1:
                    del fruitHash[fruits[leftPtr]]
                else:
                    fruitHash[fruits[leftPtr]]-=1
                leftPtr+=1
            


            maxLength=max(maxLength,i-leftPtr+1)
       # print(i,leftPtr)
        #maxLength=max(maxLength,i-leftPtr)
        return maxLength
            


        