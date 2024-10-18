from collections import deque
from typing import List


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.m = {}
        self.u = deque()
        for n in nums:
            self.add(n)

    def showFirstUnique(self) -> int:
        while self.u and self.m[self.u[0]] > 1:
            self.u.popleft()
        return self.u[0] if self.u else -1

    def add(self, val: int) -> None:
        if val not in self.m:
            self.m[val] = 1
            self.u.append(val)
        else:
            self.m[val] += 1
