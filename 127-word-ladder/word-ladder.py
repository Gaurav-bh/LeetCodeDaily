class Solution:
    def ladderLength(self, start_word: str, end_word: str, words: List[str]) -> int:
        q=deque()
        q.append(start_word)
        visited=set()
        count=0
        words=set(words)
        while len(q):
            l=len(q)
            count+=1
            
            #print(q)
            while l:
                curr=q.popleft()
                print(curr,count)
                if curr==end_word:
                    return count
                for i in range(len(curr)):
                    for j in range(26):
                        new_word=curr[:i]+chr(97+j)+curr[i+1:]
                        #print(new_word)
                        if new_word!=curr and new_word not in visited and new_word in words:
                            visited.add(new_word)
                            q.append(new_word)
                l-=1
            
        return 0
        