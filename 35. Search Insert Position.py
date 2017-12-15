## https://leetcode.com/problems/search-insert-position/description/
## Given a sorted array and a target value, return the index if the target is found.
## If not, return the index where it would be if it were inserted in order.
## Easy, 49ms, 96.75%

class Solution:
    def searchInsert(self, nums, target):
        
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        
        ## Returning i + 1 when the target gets out of for loop without returning
        ## Which menans target value is the largest
        ## Then the target will be inserted to the end
        return i + 1
        
        
        
        
