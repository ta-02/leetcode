from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        N = len(digits)
        res = []

        digitMap = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def dfs(curr, idx):
            if len(curr) == N:
                if curr != "":
                    res.append(curr)
                return
            for c in digitMap[digits[idx]]:
                dfs(curr + c, idx + 1)

        dfs("", 0)
        return res
