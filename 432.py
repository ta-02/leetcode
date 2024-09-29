class Node:
    def __init__(self, freq):
        self.freq = freq
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_to_node = {}

    def _add_node_after(self, new_node, prev_node):
        next_node = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = next_node
        next_node.prev = new_node

    def _remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def inc(self, key: str) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            next_freq = node.freq + 1
            node.keys.remove(key)
            if node.next.freq != next_freq:
                new_node = Node(next_freq)
                new_node.keys.add(key)
                self._add_node_after(new_node, node)
            else:
                node.next.keys.add(key)
            self.key_to_node[key] = (
                node.next if node.next.freq == next_freq else new_node
            )
            if not node.keys:
                self._remove_node(node)
        else:
            if self.head.next.freq != 1:
                new_node = Node(1)
                new_node.keys.add(key)
                self._add_node_after(new_node, self.head)
            else:
                self.head.next.keys.add(key)
            self.key_to_node[key] = self.head.next

    def dec(self, key: str) -> None:
        if key not in self.key_to_node:
            return
        node = self.key_to_node[key]
        node.keys.remove(key)
        if node.freq == 1:
            del self.key_to_node[key]
        else:
            prev_freq = node.freq - 1
            if node.prev.freq != prev_freq:
                new_node = Node(prev_freq)
                new_node.keys.add(key)
                self._add_node_after(new_node, node.prev)
            else:
                node.prev.keys.add(key)
            self.key_to_node[key] = (
                node.prev if node.prev.freq == prev_freq else new_node
            )
        if not node.keys:
            self._remove_node(node)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))
