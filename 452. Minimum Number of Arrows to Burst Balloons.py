## https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/
## Check website above for more details
## Medium, 135ms, 100%

class Solution:
    def findMinArrowShots(self, points):
        
        points.sort(key = lambda x: x[1])
        ans, endp = 0, float('-inf')
        for coord in points:
            if coord[0] > endp:
                endp = coord[1]
                ans += 1
        
        return ans
        
        
        ## Focus on the endpoint of the balloon
        ## Sort it according to the endpoint and loop through
        ## to see how many balloons you can burst
        ## If the starting point of the ballon is before the endpoint
        ## that balloon will also burst (since the list is sorted -> endpoint is larger)
        ## Hence, count only when the starting point is bigger than the endpoint of the previous balloon
        
        
        
