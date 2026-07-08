class Solution:
    def rob(self, nums: list[int]) -> int:
        prev1 = 0  # Represents max loot up to the previous house
        prev2 = 0  # Represents max loot up to two houses ago
        
        for n in nums:
            # Current max is either:
            # 1. Not robbing this house (sticking with prev1)
            # 2. Robbing this house (n + prev2)
            current = max(prev1, prev2 + n)
            
            # Update pointers for the next iteration
            prev2 = prev1
            prev1 = current
            
        return prev1
