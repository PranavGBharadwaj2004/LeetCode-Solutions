class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # A positive power of two has exactly one '1' bit.
        # n & (n - 1) clears the lowest set bit; result is 0 only for powers of two.
        return n > 0 and (n & (n - 1)) == 0
