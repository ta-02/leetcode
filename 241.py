from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ops = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
        }

        def backtrack(l, r):
            res = []

            for i in range(l, r):
                op = expression[i]

                if op in ops:
                    n1 = backtrack(l, i - 1)
                    n2 = backtrack(i + 1, r)

                    comp = ops[op]
                    for x in n1:
                        for y in n2:
                            res.append(comp(x, y))

            if res == []:
                res.append(int(expression[l : r + 1]))

            return res

        return backtrack(0, len(expression))
