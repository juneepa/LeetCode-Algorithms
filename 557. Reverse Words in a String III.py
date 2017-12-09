## https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
## Check website above for more details
## Example:
#3 Input: "Let's take LeetCode contest"
## Output: "s'teL ekat edoCteeL tsetnoc"
## Easy, 35ms, 94.43%

class Solution(object):
    def reverseWords(self, s):

        return " ".join(i[::-1] for i in s.split(" "))
        
        ## s.split(" ") will separate input variable by words
        ## i[::-1] will reverse each word
        ## " ".join() will "connect" each reversed word into single string with space between
        
        
        
        
