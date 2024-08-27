import heapq
from collections import defaultdict
from typing import List


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:
        adj = defaultdict(list)
        for (u, v), c in zip(edges, succProb):
            adj[u].append((c, v))
            adj[v].append((c, u))

        heap = [(-1.0, start_node)]
        dists = [0.0] * n
        dists[start_node] = 1.0

        while heap:
            prob, node = heapq.heappop(heap)
            prob = -prob

            if node == end_node:
                return prob

            for cost, nei in adj[node]:
                new_prob = prob * cost
                if new_prob > dists[nei]:
                    dists[nei] = new_prob
                    heapq.heappush(heap, (-new_prob, nei))

        return 0.0
