from collections import defaultdict
from typing import List


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        res = []
        prefix_count = defaultdict(int)

        for word in words:
            for i in range(1, len(word) + 1):
                prefix = word[:i]
                prefix_count[prefix] += 1

        for word in words:
            score = 0
            for i in range(1, len(word) + 1):
                prefix = word[:i]
                score += prefix_count[prefix]
            res.append(score)

        return res
