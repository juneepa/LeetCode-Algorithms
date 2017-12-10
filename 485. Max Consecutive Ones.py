## https://leetcode.com/problems/max-consecutive-ones/description/
## Check website above for more details
## Easy, 69ms, 89.70%

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        
        a, b = 0, 0
        for i in nums:
            if i:
                a += 1
            else:
                b = max(a, b)
                a = 0

        return max(a, b)
        
        
        
