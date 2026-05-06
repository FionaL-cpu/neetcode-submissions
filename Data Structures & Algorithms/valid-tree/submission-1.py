from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nodeMap = defaultdict(list) 
        visit = set()
        for u, v in edges:
            nodeMap[u].append(v)
            nodeMap[v].append(u)

        def dfs(curr, pre):
            if curr in visit: 
                return False 
            
            
            # recursion 
            visit.add(curr)
            for node in nodeMap[curr]:
                if node == pre: 
                    continue
                if not dfs(node,curr):
                    return False
            return True

        return dfs(0, -1) and len(visit) == n


