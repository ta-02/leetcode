import heapq
from typing import List


class Solution:
    INF = int(2e9)

    def dijkstra(self, n, source, destination, adj):
        distance = [self.INF] * n
        distance[source] = 0
        pq = []

        heapq.heappush(pq, (0, source))

        while pq:
            cost, node = heapq.heappop(pq)

            if node == destination:
                break

            for ccost, cnode in adj[node]:
                if distance[cnode] > cost + ccost:
                    distance[cnode] = cost + ccost
                    heapq.heappush(pq, (distance[cnode], cnode))

        return distance[destination]

    def modifiedGraphEdges(
        self,
        n: int,
        edges: List[List[int]],
        source: int,
        destination: int,
        target: int,
    ) -> List[List[int]]:

        adj = [[] for _ in range(n)]

        for e in edges:
            if e[2] == -1:
                continue
            adj[e[0]].append((e[2], e[1]))
            adj[e[1]].append((e[2], e[0]))

        sortedDistance = self.dijkstra(n, source, destination, adj)

        if sortedDistance < target:
            return []

        isEqual = sortedDistance == target

        for e in edges:
            if e[2] != -1:
                continue

            e[2] = self.INF if isEqual else 1
            adj[e[0]].append((e[2], e[1]))
            adj[e[1]].append((e[2], e[0]))

            if not isEqual:
                newSortedPath = self.dijkstra(n, source, destination, adj)

                if newSortedPath <= target:
                    isEqual = True
                    e[2] += target - newSortedPath
        if isEqual:
            return edges

        return []
