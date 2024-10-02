from collections import Counter
from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        f = Counter(n % k for n in arr)

        for key in f.keys():
            other_num = (k - key) % k

            if key == other_num and f[key] % 2 != 0:
                return False

            if f[key] != f[other_num]:
                return False

        return True
