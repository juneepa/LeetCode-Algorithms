## https://leetcode.com/problems/jewels-and-stones/description/
## Check website above for more details
## Easy, 70ms, No Data

class Solution:
    def numJewelsInStones(self, J, S):
        
        ans = 0
        for i in S:
            if i in J:
                ans += 1
        
        return ans
        
        
        
