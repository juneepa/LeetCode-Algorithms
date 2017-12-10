## https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
## Check website above for more details
## Easy, 249ms, 92.79%

class Solution(object):
        def findDisappearedNumbers(self, nums):
            
            return list(set(range(1, len(nums) + 1)) - set(nums))
            
            ## set(A) - set(B) gives the difference()
            ## return the list of the set difference
        
        
        
