class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1        # 2147483647
        INT_MIN = -2**31           # -2147483648

        sign = -1 if x < 0 else 1
        x_abs = -x if x < 0 else x

        res = 0
        limit = INT_MAX if sign == 1 else -INT_MIN  # 2147483647 or 2147483648

        while x_abs != 0:
            pop = x_abs % 10
            x_abs //= 10

            # Check overflow before multiplying by 10 and adding pop
            if res > limit // 10 or (res == limit // 10 and pop > limit % 10):
                return 0

            res = res * 10 + pop

        return sign * res
