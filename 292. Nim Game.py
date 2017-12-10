## https://leetcode.com/problems/nim-game/description/
## Check website above for more details
## Easy, 29ms, 51.25%


class Solution(object):
    def canWinNim(self, n):

        return n % 4 != 0
        
        ## Every 4th number, you will lose
        ## Since you can take up to 3 stones, 4 would be the unlucky number and players should avoid leaving 4 stones
        ## But other than every 4th numbers, you can leave 4 stones to the enemy players since you can take up to 3 stones.
        ## Hence, it is only every 4th stone that gives enemy players an upper hand since enemy player can always
        ## maintain 4x stones by letting the stones taken away in 2 turns 4 (i.e. (3, 1), (2, 2), and (1, 3))
               
        
        
        
        
