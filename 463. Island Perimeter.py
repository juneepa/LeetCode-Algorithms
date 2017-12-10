## https://leetcode.com/problems/island-perimeter/description/
## Check website above for more details
## Easy, 206ms, 99.30ms

class Solution(object):
    def islandPerimeter(self, grid):
        
        if not len(grid):
            return 0

        ans = 0
        
        ## Count 4 for each 1 since it has 4 sides and - 2 for each contact since one side will be counted twice 
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    ans += 4
                    if i > 0 and grid[i-1][j]:
                        ans -=2
                    if j > 0 and grid[i][j-1]:
                        ans -=2
        return ans
        

        
        
        
        
