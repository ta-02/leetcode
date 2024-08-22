from functools import cache


class Solution:
    def strangePrinter(self, s: str) -> int:
        @cache
        def dp(left, right):
            if left > right:
                return 0
            if left == right:
                return 1
            best = 1 + dp(left + 1, right)
            for mid in range(left + 1, right + 1):
                if s[left] == s[mid]:
                    best = min(best, dp(left, mid - 1) + dp(mid + 1, right))
            return best

        return dp(0, len(s) - 1)
