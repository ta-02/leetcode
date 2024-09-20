class Solution:
    def shortestPalindrome(self, s: str) -> str:
        p, suf = 0, 0
        b = 29
        power = 1
        idx = 0
        mod = 10**9 + 7

        for i, c in enumerate(s):
            char = ord(c) - ord("a") + 1

            p = (p * b) % mod
            p = (p + char) % mod

            suf = (suf + char * power) % mod
            power = (power * b) % mod

            if p == suf:
                idx = i

        suffix = s[idx + 1 :]
        return suffix[::-1] + s
