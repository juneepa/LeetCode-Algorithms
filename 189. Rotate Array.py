## https://leetcode.com/problems/rotate-array/description/
## Rotate an array of n elements to the right by k steps.
## For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

class Solution(object):
    def rotate(self, nums, k):
        
        n = len(nums)
        ## Rotating for length times keeps the original array unchanged.
        ## Only the remainder will change.
        k = k % n
        
        ## Smart way to give the answer
        ## nums[:] keeps the change inside the array
        nums[:] = nums[-k:] + nums[:-k]
