## https://leetcode.com/problems/binary-number-with-alternating-bits/description/
## Check website above for more details
## Easy, 55ms, 84.33%


class Solution:
    def hasAlternatingBits(self, n):
        
        n = bin(n)[2:]
        for i in range(1, len(n)):
            if n[i-1] == n[i]:
                return False
        
        return True
        
        
        
