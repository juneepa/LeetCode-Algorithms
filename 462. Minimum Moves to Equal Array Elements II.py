## https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description/
## Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, 
## where a move is incrementing a selected element by 1 or decrementing a selected element by 1.
## Check the link above for examples
## Medium, 43ms, 66.95%

class Solution(object):
    def minMoves2(self, nums):
        
        ## Sort the list to find the median
        nums.sort()
        
        ## Find the median
        ## Median, NOT Average, will be the parameter since it is the most "general" number of the group
        ## The differences between median and other elements are the least
        ## When len(nums) is even, choosing either one of the middle 2 will return the same answer
        ## Since there are same number of elements left and right
        med = nums[len(nums)//2]
        
        ## Count the "distance" between median and elements in the list
        ## Median - median = 0 so no need to worry about it
        return sum(abs(i - med) for i in nums)

## Same solution without any comments
class Solution(object):
    def minMoves2(self, nums):

        nums.sort()
        med = nums[len(nums)//2]
        return sum(abs(i - med) for i in nums)
