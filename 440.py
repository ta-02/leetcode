class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1
        i = 1

        def count(curr):
            res = 0
            nei = curr + 1
            while curr <= n:
                res += min(n + 1, nei) - curr
                curr *= 10
                nei *= 10
            return res

        while i < k:
            steps = count(curr)
            if i + steps <= k:
                curr += 1
                i += steps
            else:
                curr *= 10
                i += 1

        return curr
