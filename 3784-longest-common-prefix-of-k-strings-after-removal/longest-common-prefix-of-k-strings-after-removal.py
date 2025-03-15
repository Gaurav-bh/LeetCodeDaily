class Trie:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.count = 0
        
    def addWord(self, word, first_max, second_max, k):
        current = self
        flag = True
        
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if not current.children[index]:
                current.children[index] = Trie()
            current = current.children[index] 
            current.count += 1
            if current.count >= k:
                print("Yes")
                if len(first_max[0]) <= i + 1:
                    print("ha")
                    if flag: 
                        second_max[0] = first_max[0]
                    
                    first_max[0] = word[:i + 1]
                    flag = False
                elif  flag and len(second_max[0]) <= i + 1:
                    second_max[0] = word[: i + 1]
                    
                    

class Solution:
    def longestCommonPrefix(self, words: List[str], k: int) -> List[int]:
        first_max = [""]
        second_max = [""]
        
        myTrie = Trie()
        
        for i in range(len(words)):
            myTrie.addWord(words[i], first_max, second_max, k)
            print(first_max)
            print(second_max)
            
        
        answer = [0 for i in range(len(words))]
        for i in range(len(words)):
            if words[i].find(first_max[0]) == 0:
                answer[i] = len(second_max[0])
            else:
                answer[i] = len(first_max[0])
            
        
        return  answer
            
            
            