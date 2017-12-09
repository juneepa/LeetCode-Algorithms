## https://leetcode.com/problems/distribute-candies/description/
## Check website for more details
## Easy, 156ms, 67.41%

class Solution(object):
    def distributeCandies(self, candies):

        return min(len(candies)/2, len(set(candies)))
        

        ## Candies have to be distributed equally to two people regardless of types.
        ## Ideally you can distribute different candies to both but that's not always the case
        ## If there's less candy types, 
        ## giving as many different types of candies to one person would maximize the types of candies one can have
        ## so if len(candies)/2 > len(set(candies)), return len(set(candies)) <- this case one person is having all different types
        ## Else if len(candies)/2 < len(set(candies)), sadly one can't have all different types because candies must be equally distributed.
        ## Allocate len(candies)/2 different types to one person since other one needs the same amount of candies regardless of types
        ## That case, answer will be len(candies)/2
        ## Else if len(candies)/2 = len(set(candies)) then great. Most peaceful distribution
        
        
        
        
        
