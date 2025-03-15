class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.count = 0
        self.bestPrefixLength = -1
        self.isEndOfWord = False

class Solution:
    def longestCommonPrefix(self, words: List[str], k: int) -> List[int]:
        totalWords = len(words)
        result = [0] * totalWords
        if totalWords - 1 < k:
            return result
        self.root = TrieNode()
        for word in words:
            #insert the word with increasing the count by 1 (prefix count)
            self.updateTrie(word, 1, k)
        for i in range(totalWords):
            #temp deletion of the word with count decreased by 1
            self.updateTrie(words[i], -1, k)
            result[i] = self.root.bestPrefixLength
            #re-insertion of the word
            self.updateTrie(words[i], 1, k)
        return result
    
    def updateTrie(self, word: str, delta: int, k: int) -> None:
        wordLength = len(word)
        #used to store the path used during trie travesal to update the count and use the count
        nodePath = [None] * (wordLength + 1)
        depths = [0] * (wordLength + 1)
        nodePath[0] = self.root
        depths[0] = 0
        #trie insertion
        for i in range(wordLength):
            letterIndex = ord(word[i]) - ord('a')
            if nodePath[i].children[letterIndex] is None:
                nodePath[i].children[letterIndex] = TrieNode()
            nodePath[i + 1] = nodePath[i].children[letterIndex]
            depths[i + 1] = depths[i] + 1
        #increase the count of each prefix 
        for node in nodePath:
            node.count += delta
        #find the best prefix
        for i in range(wordLength, -1, -1):
            currentNode = nodePath[i]
            candidate = depths[i] if currentNode.count >= k else -1
            for childNode in currentNode.children:
                if childNode is not None:
                    candidate = max(candidate, childNode.bestPrefixLength)
            currentNode.bestPrefixLength = candidate