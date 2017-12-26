## https://leetcode.com/problems/reverse-vowels-of-a-string/description/
## Write a function that takes a string as input and reverse only the vowels of a string.
## Check website above for more details
## Easy, 99ms, 95.71%

class Solution:
    def reverseVowels(self, s):
        
        ## List makes things easier
        ## You can assign items
        s = list(s)
        i, j = 0, len(s) - 1
        ## Search from the beginning and the end and swap when the vowels are found
        
        while i < j:
            if s[i] not in "aeiouAEIOU":
                i += 1
                continue
                ## Keep searching until you find vowel
            if s[j] not in "aeiouAEIOU":
                j -= 1
                continue
                ## Do the same thing from the end to swap
                
            ## Swap the vowels found
            ## It will reverse the order since you are swapping vowels found from the start and the end
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        
        return "".join(s)
        
        
 ## Clean Version
 
 class Solution:
    def reverseVowels(self, s):
        
        s = list(s)
        i, j = 0, len(s) - 1
        
        while i < j:
            if s[i] not in "aeiouAEIOU":
                i += 1
                continue
            if s[j] not in "aeiouAEIOU":
                j -= 1
                continue
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        
        return "".join(s)
        
        
        
