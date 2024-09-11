class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = start ^ goal
        cnt = 0
        while ans:
            if ans & (1):
                cnt += 1
            ans = ans >> 1
        return cnt
