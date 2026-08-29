class Solution:
    def isHappy(self, n: int) -> bool:
        def next_num(x: int) -> int:
            s = 0
            while x > 0:
                x, digit = divmod(x, 10)
                s += digit * digit
            return s

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = next_num(n)
        return n == 1
        
