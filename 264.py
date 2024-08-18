class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_nums = [0] * n
        t1 = t2 = t3 = 0
        ugly_nums[0] = 1
        for i in range(1, n):
            ugly_nums[i] = min(
                ugly_nums[t1] * 2,
                ugly_nums[t2] * 3,
                ugly_nums[t3] * 5,
            )
            if ugly_nums[i] == ugly_nums[t1] * 2:
                t1 += 1
            if ugly_nums[i] == ugly_nums[t2] * 3:
                t2 += 1
            if ugly_nums[i] == ugly_nums[t3] * 5:
                t3 += 1
        return ugly_nums[n - 1]
