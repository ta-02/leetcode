class Solution:
    def nearestPalindromic(self, p: str) -> str:
        INF = 10**20

        N = len(p)
        first_half = p[: N // 2]

        candidates = []
        if N % 2 == 0:
            for d in [-1, 0, 1]:
                first_half_with_d = str(int(first_half) + d)
                candidates.append(first_half_with_d + first_half_with_d[::-1])
        else:
            middle = p[N // 2]
            for d in [-1, 0, 1]:
                if int(middle) + d >= 0:
                    middle_with_d = str(int(middle) + d)
                    candidates.append(first_half + middle_with_d + first_half[::-1])

        if N - 1 > 0:
            candidates.append("9" * (N - 1))
        candidates.append("9" * N)
        candidates.append("1" + "0" * (N - 2) + "1")
        candidates.append("1" + "0" * (N - 1) + "1")

        pint = int(p)
        best = INF
        best_candidate = ""

        for c in candidates:
            if abs(int(c) - pint) < best and int(c) != pint:
                best = abs(int(c) - pint)
                best_candidate = c
            if (
                abs(int(c) - pint) == best
                and int(c) != pint
                and int(c) < int(best_candidate)
            ):
                best = abs(int(c) - pint)
                best_candidate = c

        return str(best_candidate)
