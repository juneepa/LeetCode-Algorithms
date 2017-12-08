## https://leetcode.com/problems/hamming-distance/description/
## The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
## Given two integers x and y, calculate the Hamming distance
## Easy, 32ms, 55.57%

class Solution(object):
    def hammingDistance(self, x, y):

        ## Count '1' for bin(x^y)
        ## bin(x^y) returns the bitwise difference as 1
        return bin(x^y).count('1')
