from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        def less_than(x: int) -> int:
            l, pairs = 0, 0
            for r in range(n):
                while nums[r] - nums[l] > x:
                    l += 1
                pairs += r - l
            return pairs

        l, r = 0, nums[-1] - nums[0]
        while l < r:
            mid = l + (r - l) // 2
            if less_than(mid) < k:
                l = mid + 1
            else:
                r = mid
        return l
