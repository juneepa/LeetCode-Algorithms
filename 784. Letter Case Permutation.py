## https://leetcode.com/problems/letter-case-permutation/description/
## Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.
## Return a list of all possible strings we could create.
## Examples:
## Input: S = "a1b2"
## Output: ["a1b2", "a1B2", "A1b2", "A1B2"]
## Easy, 136ms, No Data

class Solution:
    def letterCasePermutation(self, S):
        ans = ['']
        for letter in S:
            ## If letter, then for both lowercase and uppercase add letter to each elements in the list
            if letter.isalpha():
                ans = [i + l for i in ans for l in [letter.upper(), letter.lower()]]
                
            ## If number, then no need to iterate. Just add number to each elements in the list    
            else:
                ans = [i + letter for i in ans]
                
        return ans
        
        
        
        
