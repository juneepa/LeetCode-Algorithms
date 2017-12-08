## https://leetcode.com/problems/single-number-iii/description/
## Given an array of numbers nums, in which exactly two elements appear only once 
## and all the other elements appear exactly twice. Find the two elements that appear only once.
## Example:
## Input: [1, 2, 1, 3, 2, 5]
## Output: [3, 5]
## Medium, 35ms, 88.51%

class Solution(object):
    def singleNumber(self, nums):

        numdict = {}
        
        ## Check elements that appear twice and once as 0 and 1, respectively
        for i in nums:
            if i in numdict:
                numdict[i] = 0
            else:
                numdict[i] = 1

        ## Simple code to return the list when the value of the number is 1 (which means it appeared only once)
        return [i for i, j in numdict.items() if j]



