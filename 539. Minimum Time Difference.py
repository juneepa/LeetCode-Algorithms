## https://leetcode.com/problems/minimum-time-difference/description/
## Given a list of 24-hour clock time points in "Hour:Minutes" format,
## Find the minimum minutes difference between any two time points in the list.
## Example:
## Input: ["23:59","00:00"]
## Output: 1
## Medium, 86ms, 96.88%, Python3

class Solution:
    def findMinDifference(self, timePoints):
        
        time = []
        for i in timePoints:
            ## 'Integerize' the str(time)
            time.append(int(i[:2]) * 60 + int(i[-2:]))
        
        time.sort()
        ## To also consider the difference in the latest time and the earliest time, add time[0] + 1440 (24 hours)
        time.append(time[0] + 1440)
        ## First to compare
        ans = time[1] - time[0]
        
        ## Save the minimum and return
        for i in range(1, len(time) - 1):
            ans = min(ans, time[i + 1] - time[i])
        
        return ans
