from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
        s=set()
        q=deque([(beginWord, 1)])
        for i in wordList:
            s.add(i)
        while q:
            word, steps=q.popleft()
            if word==endWord:
                return steps
            for i in range(len(word)):
                for ch in range(97, 123):
                    new_word=word[:i]+chr(ch)+word[i+1:]
                    if new_word in s:
                        s.remove(new_word)
                        q.append((new_word, steps+1))
        return 0