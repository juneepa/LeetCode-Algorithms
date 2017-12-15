## https://leetcode.com/problems/add-binary/description/
## Given two binary strings, return their sum (also a binary string).
## Easy, 65ms, 92.48%

class Solution:
    def addBinary(self, a, b):
        
        return bin(int(a, 2) + int(b, 2))[2:]
        
        
        
