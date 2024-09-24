from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        res = 0
        hs = set()
        for s in arr1:
            s = str(s)
            for i in range(len(s)):
                hs.add(s[0 : i + 1])

        for s in arr2:
            s = str(s)
            for i in range(len(s)):
                prefix = s[0 : i + 1]
                if prefix in hs:
                    res = max(len(prefix), res)

        return res
