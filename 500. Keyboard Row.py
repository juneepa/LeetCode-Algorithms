## https://leetcode.com/problems/keyboard-row/description/
## Check website above for more details
## Example:
## Input: ["Hello", "Alaska", "Dad", "Peace"]
## Output: ["Alaska", "Dad"]
## Easy, 29ms, 69.65%

class Solution(object):
    def findWords(self, words):

        list = []
        
        for word in words:
        
            ## Ignore Case
            word_in_set = set(word.lower())
            for i in [set('qwertyuiop'), set("asdfghjkl"), set("zxcvbnm")]:
            
                ## issubset to check if the letters of the word can be written with one keyboard row
                if word_in_set.issubset(i):
                    list.append(word)
                    ## If issubset of one of the keyboard row, there is no way the word will be subset of a different row
                    ## To save time, break
                    break
        
        return(list)
        
## Clean without comments

class Solution(object):
    def findWords(self, words):

        list = []
        
        for word in words:
            word_in_set = set(word.lower())
            for i in [set('qwertyuiop'), set("asdfghjkl"), set("zxcvbnm")]:
                if word_in_set.issubset(i):
                    list.append(word)
                    break
        
        return(list)
        
        
        
        
        
