class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases: if n is 1 or 2, return n directly
        if n <= 2:
            return n
        
        # Initialize the number of ways to reach step 1 and step 2
        a, b = 1, 2
        
        # Calculate ways to reach each step from 3 to n
        for _ in range(3, n + 1):
            a, b = b, a + b
        
        # b now contains the number of ways to reach step n
        return b
