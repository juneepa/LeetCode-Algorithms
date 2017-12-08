## https://leetcode.com/problems/teemo-attacking/description/
## Example:
## Input: [1,2], 2
## Output: 3
## Explanation: At time point 1, Teemo starts attacking Ashe and makes Ashe be poisoned. 
## This poisoned status will last 2 seconds until the end of time point 2. 
## However, at the beginning of time point 2, Teemo attacks Ashe again who is already in poisoned status. 
## Since the poisoned status won't add up together, though the second poisoning attack will still work at time point 2, it will stop at the end of time point 3. 
## So you finally need to output 3.
## Medium, 79ms, 75.41%

## Two different solutions

class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        
        if not timeSeries:
            return 0
        
        damage = 0
        for i in range(len(timeSeries) - 1):
            if timeSeries[i + 1] - timeSeries[i] + 1 > duration:
                damage += duration
            else:
                damage += (timeSeries[i + 1] - timeSeries[i])
        
        return damage + duration

## Smarter Solution
class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        
        ## Calculate the damage assuming no overlapping
        ans = duration * len(timeSeries)
        
        ## If the time between attack is greater than 0, subtract that amount from the damage
        for i in range(1,len(timeSeries)):
            ans -= max(0, duration - (timeSeries[i] - timeSeries[i-1]))
            
        return ans



