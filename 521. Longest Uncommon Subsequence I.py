## https://leetcode.com/problems/longest-uncommon-subsequence-i/description/
## Check website above for more details
## Easy, 28ms, 88.28% 

class Solution(object):
    def findLUSlength(self, a, b):
        
        ## if a == b then everything will be a subset so return -1
        ## else, return the longer one since it will not be a subset anyways...
        return -1 if a == b else max(len(a), len(b))
        
        
        
