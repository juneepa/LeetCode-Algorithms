## https://leetcode.com/problems/detect-capital/description/
## Check website above for more details
## Example:
## Input: "USA"
## Output: True
## Input: "FlaG"
## Output: False

## Easy, 35ms, 96.12%

class Solution(object):
    def detectCapitalUse(self, word):

        ## 3 cases
        ## isupper() or islower()
        ## or first letter is upper and lower afterwards
        
        ## you can use .istitle() for the 3rd case
        
        if word.isupper() or word.islower() or (word[0].isupper() and word[1:].islower()):
            return True
        else:
            return False
            
            
            
            
