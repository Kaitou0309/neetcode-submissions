class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        

        n = len(words)
        adj_list = defaultdict(list)
        
        q = deque()

       
        for i in range(len(words)-1):

            w1, w2 = words[i], words[i+1]
            
            j = 0
            k = 0

            if len(w1) > len(w2) and w2 in w1: 
                return ""

            while j < len(w1) and k < len(w2): 
                if w1[j] != w2[k]:
                    adj_list[w1[j]].append(w2[k])
                    break
                j += 1
                k += 1

        n_degrees = defaultdict(int)
        
        for k, v in adj_list.items(): 
            for i in v: 
                n_degrees[i] += 1

        for i in range(len(words)):
            for j in range(len(words[i])): 

                if words[i][j] not in n_degrees: 
                    n_degrees[words[i][j]] = 0
        
        print(adj_list)
        print(n_degrees)

        for k in n_degrees: 
            if n_degrees[k] == 0: 
                q.append(k) 
        res = ""
        while q: 
            node = q.popleft()
            res += node
            for nei in adj_list[node]: 

                n_degrees[nei] -= 1

                if n_degrees[nei] == 0: 
                    q.append(nei)

        
        for k in n_degrees: 
            if n_degrees[k] != 0: 
                return ""

        return res








                

            
