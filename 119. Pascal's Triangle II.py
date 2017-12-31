## https://leetcode.com/problems/pascals-triangle-ii/description/
## Given an index k, return the kth row of the Pascal's triangle.
## Easy, 49ms, 84.85%

class Solution:
    def getRow(self, row):
        
        if not row:
            return [1]
        if row == 1:
            return [1, 1]
        
        ## Make the "middle" part
        ans = [2]
        while row > 2:
            var = []
            for i in range(len(ans) - 1):
                var.append(ans[i] + ans[i + 1])
            ans = [ans[0] + 1] + var + [ans[len(ans) - 1] + 1]
            row -= 1
        
        ## Always [1] and [1] on the edge
        return [1] + ans + [1]
        
        
        
        
