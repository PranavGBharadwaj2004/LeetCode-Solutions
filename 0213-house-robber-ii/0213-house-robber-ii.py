class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        def rob_linear(start: int, end: int) -> int:
            prev2 = 0
            prev1 = 0
            
            for i in range(start, end + 1):
                current = max(prev1, prev2 + nums[i])
                prev2 = prev1
                prev1 = current
            
            return prev1
        
        # Case 1: rob from 0 to n-2
        # Case 2: rob from 1 to n-1
        return max(rob_linear(0, n - 2), rob_linear(1, n - 1))
