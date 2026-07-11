from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        a = ord('a')

        for s in strs:
            freq = [0] * 26
            for ch in s:
                freq[ord(ch) - a] += 1
            groups[tuple(freq)].append(s)

        return list(groups.values())
