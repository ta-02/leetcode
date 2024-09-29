class AllOne:

    def __init__(self):
        self.map = {}
        self.max = ()
        self.min = ()

    def inc(self, key: str) -> None:
        if key in self.map:
            self.map[key] += 1
        else:
            self.map[key] = 1

        if self.max:
            if self.map[key] > self.max[1]:
                self.max = (key, self.map[key])
        else:
            self.max = (key, self.map[key])

    def dec(self, key: str) -> None:
        count = self.map[key]
        if count - 1 == 0:
            self.map.pop(key)
        else:
            self.map[key] = count - 1

    def getMaxKey(self) -> str:
        if len(self.map) == 0:
            return ""

        return max(self.map)

    def getMinKey(self) -> str:
        if len(self.map) == 0:
            return ""

        return min(self.map)


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
