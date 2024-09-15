class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = "aeiou"
        mask, res = 0, 0
        mask_to_idx = {0: -1}

        for i, c in enumerate(s):
            if c in vowels:
                mask ^= ord(c) - ord("a") + 1
            if mask in mask_to_idx:
                len = i - mask_to_idx[mask]
                res = max(res, len)
            else:
                mask_to_idx[mask] = i
        return res
