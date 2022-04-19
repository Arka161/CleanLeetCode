class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # similar to NeetCode's solution
        
        adj = {src: [] for src, dst in tickets}
        
        # Might require a different comparator in another language
        tickets.sort()
        
        for src, dst in tickets: 
            adj[src].append(dst)
            
        res = ["JFK"]
        
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            
            if src not in adj:
                return False
            
            temp = list(adj[src])
            
            for i, v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)
                if dfs(v):
                    return True
                adj[src].insert(i, v)
                res.pop()
            return False
        dfs("JFK")
        return res