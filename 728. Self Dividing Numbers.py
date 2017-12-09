## https://leetcode.com/problems/self-dividing-numbers/description/
## Check website above for more details
## Easy, 46ms, 96.14%
## Contains two solutions

## Simple but slower solution
class Solution(object):
    def selfDividingNumbers(self, left, right):
        
        ans = []
        for num in range(left, right + 1):
            ## add to the answer list only if it satisfies all the condition
            if all(int(i) and not num % int(i) for i in str(num)):
                ans.append(num)
        
        return ans
        
## Faster Solution        
class Solution(object):
    def selfDividingNumbers(self, left, right):
    
        ans = []
        for i in range(left, right+1):
            num = i
            while num:
                if not num % 10:
                    break
                if i % (num % 10):
                    break
                num /= 10
            if not num:
                ans.append(i)
        return ans
        
        
        
        
