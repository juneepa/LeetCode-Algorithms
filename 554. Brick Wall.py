## https://leetcode.com/problems/brick-wall/description/
## Medium, 66ms, 91.01%

class Solution(object):
    def leastBricks(self, walls):
        
        ## Create a default dictionary
        spread = collections.defaultdict(int)
        
        ## Create sort of a graph regarding the length of the bricks
        for wall in walls:
            i = 0
            for brick in wall[:-1]:
                i += brick
                spread[i] += 1
        
        ## the max(spread.values()) will represent how many bricks hit the certain length x
        ## Subtracting that from the length of the walls will give the least amount of bricks to penetrate
        ## +[0] in case when spread.values() is empty (ex walls = [[1],[1],[1]])
        return len(walls) - max(spread.values() + [0])
    
#Clean Solution without comments

class Solution(object):
    def leastBricks(self, walls):
        
        spread = collections.defaultdict(int)
        for wall in walls:
            i = 0
            for brick in wall[:-1]:
                i += brick
                spread[i] += 1
        
        return len(walls) - max(spread.values() + [0])
 




