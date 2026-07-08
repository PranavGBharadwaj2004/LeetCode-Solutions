class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize current_sum to 0 and max_sum to the first element
        # to handle cases where all numbers might be negative.
        max_sum = nums[0]
        current_sum = 0
        
        for num in nums:
            # If current_sum becomes negative, reset it to 0
            if current_sum < 0:
                current_sum = 0
            
            # Add the current number to the sum
            current_sum += num
            
            # Update the global maximum sum found so far
            max_sum = max(max_sum, current_sum)
            
        return max_sum
