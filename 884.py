from typing import Counter, List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        f = Counter(s1.split() + s2.split())
        return list(filter(lambda x: f[x] == 1, f))
