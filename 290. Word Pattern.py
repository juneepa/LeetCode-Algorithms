## https://leetcode.com/problems/word-pattern/description/
## Given a pattern and a string str, find if str follows the same pattern.
## Here follow means a full match,
## such that there is a bijection between a letter in pattern and a non-empty word in str.
## Easy, 49ms, 63.30%

## 2 different solutions

## Solution #1
class Solution:
    def wordPattern(self, pattern, strs):
        
        strs = strs.split(" ")
        if len(pattern) != len(strs):
            return False
        
        sdict, pdict = {}, {}
        for i in range(len(strs)):
        
            ## If strs[i] not in sdict, it will return null instead of key error
            if sdict.get(strs[i]) != pdict.get(pattern[i]):
                return False
                
            sdict[strs[i]] = pdict[pattern[i]] = i

        return True
   
 ## Solution #2
 class Solution:
  def wordPattern(self, pattern, strs):

      strs = strs.split(" ")
      if len(pattern) != len(strs):
          return False

      sdict = {}
      for i in range(len(strs)):
      
          ## If not in the dictionary, check if the pattern value is already inside
          ## to prevent algorithm assigning str to the existing pattern
          if strs[i] not in sdict:
              if pattern[i] in sdict.values():
                  return False
              sdict[strs[i]] = pattern[i]
          
          ## Add to the dictionary
          else:
              if sdict[strs[i]] != pattern[i]:
                  return False

      return True     

