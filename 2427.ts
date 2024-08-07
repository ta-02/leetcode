function commonFactors(a: number, b: number): number {
  const min = a > b ? b : a;
  let ans = 0;
  for (let i = 1; i <= min; i++) {
    if (a % i === 0 && b % i === 0) ans++;
  }
  return ans;
}
