class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        pattern_map = defaultdict(list)

        for w in wordList:

            for i in range(len(w)):

                pattern = w[:i] + "*" + w[i+1:]
                pattern_map[pattern].append(w)


        q = deque()
        visited = set()
        
        q.append((beginWord, 1))
        visited.add(beginWord)

        while q: 
            word, dist = q.popleft()

            if word == endWord:
                return dist

            patterns = []
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                patterns.append(pattern)

            for p in patterns:
                transition_word = pattern_map[p]

                for nei in transition_word: 

                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, dist + 1))

        return 0