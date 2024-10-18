from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        clones = {}

        def dfs(node):
            if not node:
                clones[node] = None
                return

            clones[node] = Node(node.val)

            for n in node.neighbors:
                if n not in clones:
                    clones[n] = Node(n.val)
                    dfs(n)
                clones[node].neighbors.append(clones[n])

        dfs(node)
        return clones[node]
