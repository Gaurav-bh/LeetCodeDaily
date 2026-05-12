from typing import List


class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = [None] * 26


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.result_buffer = []

    # Insert a word into trie
    def insert(self, word: str) -> None:
        curr = self.root

        for ch in word:
            idx = ord(ch) - ord('a')

            if curr.children[idx] is None:
                curr.children[idx] = TrieNode()

            curr = curr.children[idx]

        curr.is_word = True

    # DFS to collect at most 3 words
    def dfs_with_prefix(self, curr: TrieNode, word: str) -> None:
        if len(self.result_buffer) == 3:
            return

        if curr.is_word:
            self.result_buffer.append(word)

        for i in range(26):
            if curr.children[i]:
                ch = chr(i + ord('a'))
                self.dfs_with_prefix(curr.children[i], word + ch)

    # Get words starting with prefix
    def get_words_starting_with(self, prefix: str) -> List[str]:
        curr = self.root
        self.result_buffer = []

        # Traverse trie till end of prefix
        for ch in prefix:
            idx = ord(ch) - ord('a')

            if curr.children[idx] is None:
                return []

            curr = curr.children[idx]

        self.dfs_with_prefix(curr, prefix)

        return self.result_buffer


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()

        # Insert all products into trie
        for product in products:
            trie.insert(product)

        result = []
        prefix = ""

        for ch in searchWord:
            prefix += ch
            result.append(trie.get_words_starting_with(prefix))

        return result