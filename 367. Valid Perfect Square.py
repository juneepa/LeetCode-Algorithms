## https://leetcode.com/problems/valid-perfect-square/description/
## Given a positive integer num, write a function which returns True if num is a perfect square else False.
## Note: Do not use any built-in library function such as sqrt.
## Easy, 49ms, 81.25%


class Solution:
    def isPerfectSquare(self, num):
        
        left, right = 0, num
        while left < right:
        
            ## To minimize the unnecessary search step from 1, choose the middle (Similar to Root Finding in Mathematics)
            ## Find the middle number, check, and move right or left accordingly to "capture" the root"
            
            middle = left + int((right - left) / 2)
            if middle ** 2 == num:
                return True
            elif middle ** 2 > num:
                right = middle - 1
            else:
                left = middle + 1
        
        ## at this point, left and right will be the same
        ## Check the last value unchecked and return boolean
        return True if left ** 2 == num else False
        
        
        
        
