from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        curr = [0, 0]
        max_distance = 0
        obstacles_set = set(map(tuple, obstacles))
        directionMap = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0],
        ]
        idx = 0

        for c in commands:
            if c == -2:
                idx = (idx + 3) % 4
            elif c == -1:
                idx = (idx + 1) % 4
            else:
                for _ in range(c):
                    mv = [
                        curr[0] + directionMap[idx][0],
                        curr[1] + directionMap[idx][1],
                    ]
                    if tuple(mv) in obstacles_set:
                        break
                    curr = mv
                    max_distance = max(max_distance, curr[0] ** 2 + curr[1] ** 2)

        return max_distance
