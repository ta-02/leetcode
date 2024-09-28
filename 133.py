from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


"""
1 -> 2, 3
2 -> 3, 4
3 -> 4


"""


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return

        q = [node]
        while q:
            curr = q.pop()
            new_curr = Node(curr.val)
            for n in curr.neighbors:
                new_n = Node(n.val)

        return None
