class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                # The problem asks for 1-indexed results
                return [left + 1, right + 1]
            elif current_sum < target:
                # Sum is too small, need a larger number, move left pointer right
                left += 1
            else:
                # Sum is too large, need a smaller number, move right pointer left
                right -= 1
