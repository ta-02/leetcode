import heapq
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []
        heap = []

        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))

        res.append(-heap[0][0])

        for i in range(k, n):
            heapq.heappush(heap, (-nums[i], i))
            while heap[0][1] <= i - k:
                heapq.heappop(heap)
            res.append(-heap[0][0])

        return res
