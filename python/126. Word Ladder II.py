from collections import defaultdict, deque

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return []

        wordSet = set(wordList)
        wordSet.add(beginWord)

        l = len(beginWord)
        intState = defaultdict(list)
        for word in wordSet:
            for i in range(l):
                intState[word[:i] + "*" + word[i+1:]].append(word)

        q = deque([beginWord])
        visited = {beginWord}
        parents = defaultdict(set)
        found = False

        while q and not found:
            currLevel = set()
            for _ in range(len(q)):
                currWord = q.popleft()
                for i in range(l):
                    intWord = currWord[:i] + "*" + currWord[i+1:]
                    for possibleNext in intState[intWord]:
                        if possibleNext in visited:
                            continue
                        parents[possibleNext].add(currWord)
                        if possibleNext == endWord:
                            found = True
                        if possibleNext not in currLevel:
                            currLevel.add(possibleNext)
                            q.append(possibleNext)
            visited |= currLevel

        if not found:
            return []

        result = []

        def backTrack(word, path):
            if word == beginWord:
                result.append(list(reversed(path)))
                return
            for parent in parents[word]:
                path.append(parent)
                backTrack(parent, path)
                path.pop()

        backTrack(endWord, [endWord])
        return result