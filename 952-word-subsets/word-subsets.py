from collections import Counter

class Solution:
    def wordSubsets(self, words1, words2):
        need = [0] * 26

        for word in words2:
            count = Counter(word)
            for ch in count:
                need[ord(ch) - ord('a')] = max(need[ord(ch) - ord('a')], count[ch])

        res = []
        for word in words1:
            count = Counter(word)
            ok = True
            for i in range(26):
                if count.get(chr(i + ord('a')), 0) < need[i]:
                    ok = False
                    break
            if ok:
                res.append(word)

        return res
