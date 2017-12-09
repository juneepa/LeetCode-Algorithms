## https://leetcode.com/problems/array-partition-i/description/
## Given an array of 2n integers, your task is to group these integers into n pairs of integer,
## say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.
## Easy, 108ms, 95.74%

class Solution(object):
    def arrayPairSum(self, nums):
        
        ## To minimize the "minimum()" effect, grouping numbers close to each other is necessary.
        ## So sort the list and group two elements consecutively
        ## Since the list is sorted, minimum() will return the first value
        ## Also, len(nums) == 2n
        ## Hence, the numbers in index 0, 2, 4, 6, .... will be added to the answer
        ## Below is the one line of code that does what I described above
        
        return sum(sorted(nums)[::2])
