## https://leetcode.com/problems/arranging-coins/description/
## Check website for more details
## Easy, 102ms, 94.44%

## Two different solutions

## First
## Straightforward Solution
class Solution:
    def arrangeCoins(self, n):

        ans = 0
        while n > 0:
            ans += 1
            n -= ans

        return ans - 1 if n else ans
        
## Second
## We are trying to find
## 1+2+3+4+....+x <= n
## then x(x+1)/2 <= n
## If we find x....

class Solution:
    def arrangeCoins(self, n):

        return math.floor(0.5*(math.sqrt(1+8*n)-1.0))
        
        
        
