class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        
        # Pointers for a and b starting from the end (least significant bit)
        i, j = len(a) - 1, len(b) - 1
        
        while i >= 0 or j >= 0 or carry:
            # Get the current bit from a and b if available, else 0
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0
            
            # Calculate the sum of bits and carry
            total = bit_a + bit_b + carry
            
            # Current bit to add to result is total % 2
            result.append(str(total % 2))
            
            # Update carry for next iteration
            carry = total // 2
            
            # Move to the next bits
            i -= 1
            j -= 1
        
        # Since we added bits from least significant to most, reverse the result
        return ''.join(result[::-1])
