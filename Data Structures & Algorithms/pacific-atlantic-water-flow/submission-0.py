class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set() #tracking visited positions 
        rows, cols = len(heights), len(heights[0])
        output =[]


        def dfs(r, c, visit, preH):
            if r < 0 or c < 0 or r >= rows or c >= cols or heights[r][c] < preH or (r,c) in visit:
                return 
            # add to visit set 
            visit.add((r,c))
            # update height 
            # recursion 
            preH = heights[r][c]
            dfs(r + 1, c, visit, preH)
            dfs(r - 1, c, visit, preH)
            dfs(r, c + 1, visit, preH)
            dfs(r, c - 1, visit, preH)
    


        for r in range(rows): 
            # r, 0; 0, cols
            dfs(r, 0, pac, heights[r][0]) 
            dfs(r, cols -1, atl, heights[r][cols - 1])

        for c in range(cols):
            # 0, c; rows-1, c;
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])
    



        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    output.append([r,c])
        
        
                    





        return output