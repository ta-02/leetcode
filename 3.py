class Solution:
    def lengthOfLongestSubstring(self, w: str) -> int:
        res = 0
        s = set()
        l, r = 0, 0

        while r < len(w):
            if w[r] in s:
                s.remove(w[l])
                l += 1
            else:
                s.add(w[r])
                res = max(res, r - l + 1)
                r += 1

        return res
