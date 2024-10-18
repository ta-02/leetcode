from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def max_sub_arr(a, i, j):
            if i == j:
                return a[j]

            m = (i + j) // 2
            v1 = max_sub_arr(a, i, m)
            v2 = max_sub_arr(a, m + 1, j)
            v3 = max_cross(a, i, m, j)

            return max(v1, v2, v3)

        def max_cross(a, low, m, high):
            left_sum = float("-inf")
            sum = 0
            for i in range(m, low - 1, -1):
                sum += a[i]
                left_sum = max(left_sum, sum)

            right_sum = float("-inf")
            sum = 0
            for i in range(m + 1, high + 1):
                sum += a[i]
                right_sum = max(right_sum, sum)

            return left_sum + right_sum

        return max_sub_arr(nums, 0, len(nums) - 1)
