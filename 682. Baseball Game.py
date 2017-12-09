## https://leetcode.com/problems/baseball-game/description/
## Check website above for more details
## Easy, 39ms, 63.00%

class Solution(object):
    def calPoints(self, ops):
        
        score = []
        for i in ops:
            if i == "C":
                score.pop()
            elif i == "D":
                score.append(score[-1] * 2)
            elif i == "+":
                score.append(score[-1] + score[-2])
            else:
                score.append(int(i))
        return sum(score)
                
                
                
                
                
                
                
                
                
                
                
                
