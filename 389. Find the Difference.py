## https://leetcode.com/problems/find-the-difference/description/
## Check website above for more details
## Given two strings s and t which consist of only lowercase letters.
## String t is generated by random shuffling string s and then add one more letter at a random position.
## Find the letter that was added in t.
## Easy, 32ms, 96.00%

class Solution(object):
    def findTheDifference(self, s, t):
        
        for i in t:
            if t.count(i) > s.count(i):
                return i
                
            ## ">" since t.count(i) will only be bigger
                
                
