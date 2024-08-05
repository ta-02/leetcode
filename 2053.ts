function kthDistinct(arr: string[], k: number): string {
  const countMap = new Map<string, number>();
  arr.forEach((x) => countMap.set(x, (countMap.get(x) || 0) + 1));
  return arr.filter((x) => countMap.get(x) === 1)[k - 1] ?? "";
}
