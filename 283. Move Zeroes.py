## https://leetcode.com/problems/move-zeroes/description/
## Check website above for more details
## Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
## For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
## Easy, 59ms, 52.92%

class Solution(object):
    def moveZeroes(self, nums):
    
        ## "Move" all the non-zero elements to the left side
        index = 0
        for i in nums:
            if i:
                nums[index] = i
                index += 1
        
        ## And change everything 0 on the right side of the index
        for i in range(index, len(nums)):
            nums[i] = 0
            
            
            
            
