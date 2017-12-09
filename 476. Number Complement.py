## https://leetcode.com/problems/number-complement/description/
## Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.
## Check Website above for more details
## Example:
## Input: 5 (101)
## Output: 2 (010)
## Easy, 29ms, 83.42%

## Two different solutions, smarter solution below

## Straight Approach
class Solution(object):
    def findComplement(self, num):
        
        ## Binary number string
        binum = bin(num)[2:]
        answer = 0
        
        ## Since 0 -> 1, whenever 0, add 2*index to the answer
        for i, n in enumerate(binum[::-1]):
            if n == '0':
                answer += 2 ** i
        
        return(answer)
        
## Smarter Solution        
class Solution(object):
    def findComplement(self, num):
        
        ## i will be bitwise "longer"
        i = 1
        while i <= num:
            i = i << 1
            
        ## i - 1 to create bitwise 1s as "long" as num
        ## xor to compare -> (0, 1) -> 1 and (1, 1) -> 0, it will return the number complement
        return (i - 1) ^ num
