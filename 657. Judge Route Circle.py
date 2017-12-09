## https://leetcode.com/problems/judge-route-circle/description/
## Initially, there is a Robot at position (0, 0). Given a sequence of its moves,
## judge if this robot makes a circle, which means it moves back to the original place.
## Example:
## Input: "UD"
## Output: True
## Easy, 35ms, 93.88%

class Solution(object):
    def judgeCircle(self, moves):
        
        ## Order of the if statement is important
        ## To come back to its origin, number of Us and Ds must be the same as well as number of Rs and Ls
        ## Check them and return false if either one of the statements does not satisfy
        ## If the program can pass those if statements, we can say the robot returns to the origin
        if moves.count("U") != moves.count("D"):
            return False
        if moves.count("R") != moves.count("L"):
            return False
        
        return True
