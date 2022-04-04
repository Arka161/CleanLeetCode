class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c: [] for c in range(numCourses)}
        
        for cre, pre in prerequisites:
            prereq[cre].append(pre)
        
        output = []
        
        visit, cycle = set(), set()
        
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit: 
                return True
            
            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
                
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            
            
        for i in range(numCourses):
            if dfs(i) == False:
                return []
        return output