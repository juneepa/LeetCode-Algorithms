## https://leetcode.com/problems/fizz-buzz/description/
## Check website above for more details
## n = 15,
## Return: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
## Easy, 72ms, 61.55%

class Solution(object):
    def fizzBuzz(self, n):
        
        ans = []
        for num in range(1, n+1):
            if not num % 15:
                ans.append("FizzBuzz")
            elif num % 3 == 0:
                ans.append("Fizz")
            elif num % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(num))
            
        return ans
        
        
        
        
