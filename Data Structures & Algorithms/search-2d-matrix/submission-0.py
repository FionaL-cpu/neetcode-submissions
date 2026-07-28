class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        
        upperleft, downleft = 0, rows - 1 
        upperright, downright = 0, rows - 1 
        target_row = -1

        while upperleft <= downleft: 

            midleft = (upperleft + downleft) // 2

            if matrix[midleft][0] > target: 
                downleft = midleft - 1 
                
            elif matrix[midleft][0] < target: 

                upperleft = midleft + 1 
                
            else:
                return True 
            
        target_row = upperleft - 1 
        if target_row < 0 and target_row > rows - 1: 
            return False 


        l, r = 0, cols - 1 
        while l <= r:
            mid = (l + r) // 2
            if matrix[target_row][mid] > target: 
                r = mid - 1
            elif matrix[target_row][mid] < target: 
                l = mid + 1
            else: 
                return True 
        return False 