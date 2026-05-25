class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        pattern_map = defaultdict(list)

        for word in wordList: 
            for i in range(len(word)): 
                pattern = word[:i] + "*" + word[i+1:]
                pattern_map[pattern].append(word)

        q = deque() 
        visited = set() 
        
        q.append((beginWord, 1))
        visited.add(beginWord)

        while q: 
            curr, dis = q.popleft() 

            if curr == endWord: 
                return dis 

            patterns = []
            for i in range(len(curr)): 
                pattern = curr[:i] + "*" + curr[i+1:]
                patterns.append(pattern)

            for p in patterns: 
                transition_words = pattern_map[p]

                for nei in transition_words: 

                    if nei not in visited: 
                        visited.add(nei)
                        q.append((nei, dis + 1))
                        

        return 0
        