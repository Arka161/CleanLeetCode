class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adjList = []
        
        initComp = len(isConnected)
        
        for index, val in enumerate(isConnected):
            innerList = val
            for index2, val2 in enumerate(innerList):
                if index != index2 and val2 == 1:
                    insertL = sorted([index, index2])
                    if insertL not in adjList:
                        adjList.append(insertL)
        length_v = len(adjList)
        
        
        
        par = [i for i in range(initComp)]
        rank = [1] * initComp
        
        #print("Parent is", par)
        #print("Rank is", rank)
        
        #print("adj List is ", adjList)
        
        def find(n):
            #print("n here is", n)
            p = par[n]
            
            while p != par[p]:
                p = par[p]
            return p
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            if p1 == p2:
                return 0
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return 1
            
        
        ans = len(isConnected)
        for n1, n2 in adjList:
            ans -= union(n1, n2)
        return ans