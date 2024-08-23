from fractions import Fraction as F


class Solution:
    def fractionAddition(self, expression: str) -> str:

        r = F()
        c = ""
        for i, x in enumerate(expression):
            if x in ("-", "+") and i > 0:
                r += F(c)
                c = ""
            c += x
        r += F(c)

        if r.denominator == 1:
            return str(r) + "/1"
        return str(r)
