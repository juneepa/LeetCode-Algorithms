## https://leetcode.com/problems/remove-element/description/
## Given an array and a value, remove all instances of that value in-place and return the new length.
## Check website above for more details
## Easy, 55ms, 84.78%

class Solution:
    def removeElement(self, nums, val):
        
        try:
            while True:
                ## Pop until you can't
                nums.pop(nums.index(val))
        except:
            pass
            
            
            
            
            
