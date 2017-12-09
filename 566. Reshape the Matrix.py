## https://leetcode.com/problems/reshape-the-matrix/description/
## Check website above for more details
## Easy, 165ms, 42.75%
## Not a great work but very straightforward

class Solution(object):
    def matrixReshape(self, nums, r, c):
        
        ## check if r and c make sense
        if r * c != len(sum(nums, [])):
            return nums
                
        flat = sum(nums, [])
        new = [[None] * c for _ in range(r)]
        a = 0
        
        for i in range(r):
            for j in range(c):
                new[i][j] = flat[a]
                a += 1            

        return new
                    
                    
                    
                    
