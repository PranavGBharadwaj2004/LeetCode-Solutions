from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count the frequency of each element
        count = Counter(nums)
        
        # 2. Create buckets where the index is the frequency
        # The maximum possible frequency is the length of the array
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in count.items():
            buckets[freq].append(num)
            
        # 3. Iterate from the back (highest frequency) to the front
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res
