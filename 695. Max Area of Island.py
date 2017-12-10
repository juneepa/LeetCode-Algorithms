## https://leetcode.com/problems/max-area-of-island/description/
## Check website above for more details
## Easy, 158ms, 82.58%

class Solution:
    def maxAreaOfIsland(self, grid):
        
        m, n = len(grid), len(grid[0])
        
        ## Recursion to expand the checking area
        ## Keep the area checked 0 to prevent double-checking
        def areacheck(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j]:
                grid[i][j] = 0
                return 1 + areacheck(i-1, j) + areacheck(i+1, j) + areacheck(i, j-1) + areacheck(i, j+1)
            return 0
        
        ## store the areas in the list
        ## since checked value will be 0, the list won't double check
        ## return the max value of the area or 0 if there's no area
        
        area = [areacheck(i, j) for i in range(m) for j in range(n) if grid[i][j]]
        return max(area) if area else 0
        
## Clean solution without comments        
class Solution:
    def maxAreaOfIsland(self, grid):
        
        m, n = len(grid), len(grid[0])
        
        def areacheck(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j]:
                grid[i][j] = 0
                return 1 + areacheck(i-1, j) + areacheck(i+1, j) + areacheck(i, j-1) + areacheck(i, j+1)
            return 0
        
        area = [areacheck(i, j) for i in range(m) for j in range(n) if grid[i][j]]
        return max(area) if area else 0   
        
        
        
        
