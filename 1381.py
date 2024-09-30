class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.size = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.size:
            self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1

        return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        if k > len(self.stack):
            self.stack = list(map(lambda x: x + val, self.stack))
        else:
            for i in range(k):
                self.stack[i] += val
