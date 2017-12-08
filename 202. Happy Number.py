## https://leetcode.com/problems/happy-number/description/
## Example: 19 is a happy number
## 1^2 + 9^2 = 82
## 8^2 + 2^2 = 68
## 6^2 + 8^2 = 100
## 1^2 + 0^2 + 0^2 = 1

## n is positive integer

class Solution:
    def isHappy(self, n):
        
        ## Recursion process to calculate the single step
        def process(n):
            return n ** 2 if n < 10 else (n % 10) ** 2 + process(n // 10)
        
        ## Add the result to the set to check whether "process" is going to be an infinite loop or not
        ## If n != 1 is already in the set "seen", that means the loop is going to be infinite
        ## n == 1 will stop the while loop since 1^2 = 1
        seen = set()
        while n not in seen:
            seen.add(n)
            n = process(n)
        
        ## Simple code to return True or False according to n
        return n == 1
