from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def partition(arr, low, high):
            pivot = arr[high]

            i = low - 1

            for j in range(low, high):
                if arr[j] <

        # def merge(a: List[int], l: int, m: int, r: int) -> None:
        #     left = a[l : m + 1]
        #     right = a[m + 1 : r + 1]
        #
        #     i = j = 0
        #     k = l
        #
        #     while i < len(left) and j < len(right):
        #         if left[i] <= right[j]:
        #             a[k] = left[i]
        #             i += 1
        #         else:
        #             a[k] = right[j]
        #             j += 1
        #         k += 1
        #
        #     while i < len(left):
        #         a[k] = left[i]
        #         i += 1
        #         k += 1
        #
        #     while j < len(right):
        #         a[k] = right[j]
        #         j += 1
        #         k += 1
        #
        # def merge_sort(a: List[int], l: int, r: int) -> None:
        #     if l < r:
        #         m = (l + r) // 2
        #         merge_sort(a, l, m)
        #         merge_sort(a, m + 1, r)
        #         merge(a, l, m, r)
        #
        # merge_sort(nums, 0, len(nums) - 1)
        # return nums
        return nums
