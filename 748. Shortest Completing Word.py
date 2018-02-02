## https://leetcode.com/problems/shortest-completing-word/discuss/
## Check website above for more details
## Medium, 192ms, No Data

class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        
        ans = None
        
        ## Count alphabets
        wdict = collections.Counter(letter.lower() for letter in licensePlate if letter.isalpha())
        
        for word in words:
        
            ## Check if the word uses all the alphabets required
            ## change ans only if the word is shorter (as required in the question)
            if (not ans or len(ans) > len(word)) and not wdict - collections.Counter(word):
                ans = word
        
        return ans
        
        
        
        
