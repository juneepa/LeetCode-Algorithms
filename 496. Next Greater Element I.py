## https://leetcode.com/submissions/detail/131412729/
## Check website above for more details
## Easy, 99ms, 31.06%

class Solution(object):
    def nextGreaterElement(self, n1, n2):
      
        def compare(a, b):
            ## Start checking from the specific number index
            for i in b[b.index(a):]:
                if a < i:
                    return i
            return -1
        
        return [compare(i, n2) for i in n1]
        
        
        
        
