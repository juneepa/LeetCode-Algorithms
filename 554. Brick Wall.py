class Solution(object):
    def leastBricks(self, walls):
        
        spread = collections.defaultdict(int)
        for wall in walls:
            i = 0
            for brick in wall[:-1]:
                i += brick
                spread[i] += 1
        
        return len(walls) - max(spread.values() + [0])
 