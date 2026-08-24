from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        # Traverse the digits array from the end to the beginning
        for i in range(n - 1, -1, -1):
            # If the current digit is less than 9, just add one and return the array
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If the digit is 9, it becomes 0 and carry over to the next digit
            digits[i] = 0
        
        # If all digits were 9, then the result is a 1 followed by n zeros
        return [1] + [0] * n
