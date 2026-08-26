from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []
        res: List[List[int]] = [[1]]
        for _ in range(1, numRows):
            prev = res[-1]
            # build next row using neighbors from previous row
            row = [1] + [prev[i - 1] + prev[i] for i in range(1, len(prev))] + [1]
            res.append(row)
        return res
