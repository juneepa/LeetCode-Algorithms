## https://leetcode.com/problems/add-digits/description/
## Check website above for more details
## Could you do it without any loop/recursion in O(1) runtime?
## Easy, 32ms, 97.82%

class Solution(object):
    def addDigits(self, num):

        return num % 9 if num % 9 else 9 if num else 0

        ## 1 % 9 = 1
        ## 10 % 9 = 1
        ## 100 % 9 = 1
        ## ....
        ## Hence, %9 will return the "digit" value
        ## However, 9 % 9 = 0. We need special care on that case
        ## when num % 9 = 0, num is either 9 or 0
        ## return 0 if num is 0 or else 9
        
        
        
