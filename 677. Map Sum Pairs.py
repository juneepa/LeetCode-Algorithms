## https://leetcode.com/problems/map-sum-pairs/description/
## Implement a MapSum class with insert, and sum methods.
## Check website above for more details
## Medium, 44ms, 100%

class MapSum:

    ## Initialize the dictionary
    def __init__(self):
        self.wdict = {}

    ## Insert keys and value
    ## Since values will be overrided for the already existing key, just one line below will be enough
    def insert(self, key, val):
        self.wdict[key] = val

    ## if the first len(prefix) letters equals to the prefix, add the key to the sum
    def sum(self, prefix):
        sum = 0
        for key in self.wdict:
            if key[:len(prefix)] == prefix:
                sum += self.wdict[key]
        return sum
        
 ## Clean       
 class MapSum:

    def __init__(self):
        self.wdict = {}

    def insert(self, key, val):
        self.wdict[key] = val

    def sum(self, prefix):
        sum = 0
        for key in self.wdict:
            if key[:len(prefix)] == prefix:
                sum += self.wdict[key]
        return sum
        
        
        
        
