function rangeSum(
  nums: number[],
  n: number,
  left: number,
  right: number,
): number {
  const sumArray: number[] = [];

  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j <= nums.length; j++) {
      sumArray.push(nums.slice(i, j).reduce((arr, x) => arr + x, 0));
    }
  }

  const ans = sumArray
    .sort((a, b) => a - b)
    .slice(left - 1, right)
    .reduce((arr, x) => arr + x, 0);

  return ans % (Math.pow(10, 9) + 7);
}

console.log(rangeSum([1, 2, 3, 4], 4, 1, 5));
