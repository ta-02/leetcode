function minSwaps(nums: number[]): number {
  const N = nums.length;
  const windowSize = nums.reduce((acc, num) => acc + num, 0);

  let initialWindowOnes = nums
    .slice(0, windowSize)
    .reduce((acc, num) => acc + num, 0);

  let windowOnes = initialWindowOnes;
  let maxWindowOnes = windowOnes;

  for (let i = 1; i < N; i++) {
    windowOnes -= nums[i - 1];
    windowOnes += nums[(i + windowSize - 1) % N];
    maxWindowOnes = Math.max(maxWindowOnes, windowOnes);
  }

  return windowSize - maxWindowOnes;
}
