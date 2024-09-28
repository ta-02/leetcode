class MyCircularDeque:

    def __init__(self, k: int):
        self.cap = k
        self.q = []

    def insertFront(self, value: int) -> bool:
        if len(self.q) == self.cap:
            return False

        self.q.insert(0, value)
        return True

    def insertLast(self, value: int) -> bool:
        if len(self.q) == self.cap:
            return False

        self.q.append(value)
        return True

    def deleteFront(self) -> bool:
        if len(self.q) == 0:
            return False
        self.q = self.q[1:]
        return True

    def deleteLast(self) -> bool:
        if len(self.q) == 0:
            return False

        self.q = self.q[: len(self.q) - 1]
        return True

    def getFront(self) -> int:
        if len(self.q) == 0:
            return -1
        return self.q[-1]

    def getRear(self) -> int:
        if len(self.q) == 0:
            return -1
        return self.q[len(self.q)]

    def isEmpty(self) -> bool:
        return len(self.q) == 0

    def isFull(self) -> bool:
        return len(self.q) == self.cap
