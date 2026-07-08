class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        # Determine the maximum value to know the size of our points array
        max_val = max(nums)
        points = [0] * (max_val + 1)
        
        # Calculate the total value for each number
        for num in nums:
            points[num] += num
        
        # Apply the House Robber logic
        prev2 = 0
        prev1 = 0
        
        for val in points:
            # At each step, either take the current points + skip previous,
            # or keep the previous total
            current = max(prev1, prev2 + val)
            prev2 = prev1
            prev1 = current
            
        return prev1
