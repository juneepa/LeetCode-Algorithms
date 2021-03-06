## https://leetcode.com/problems/single-number/
## Given an array of integers, every element appears twice except for one. Find that single one.

## Contains two different solutions

## Initial Attempt
class Solution(object):
    def singleNumber(self, nums):
        
        ndict = {}
        ## Checkmark the number that appears twice as 1
        for i in nums:
            if i in ndict:
                ndict[i] = 1
            else:
                ndict[i] = 0
        
        ## Return the key that has value 0
        for i in ndict:
            if not ndict.get(i):
                return i
                
## Smarter Solution                
class Solution(object):        
    def singleNumber3(self, nums):
        ## Since numbers appear twice except one
        ## Twice the sum of the unique number set minus sum of the original list will return the value
        return 2 * sum(set(nums)) - sum(nums)
