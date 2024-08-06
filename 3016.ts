function minimumPushes(word: string): number {
  const countMap = word.split("").reduce((map, x) => {
    map.set(x, (map.get(x) || 0) + 1);
    return map;
  }, new Map<string, number>());

  const sortedMap = new Map(
    [...countMap.entries()].sort((a, b) => b[1] - a[1]),
  );

  let ans = 0;
  let count = 0;

  sortedMap.forEach((v) => {
    const level = Math.floor(count / 8) + 1;
    ans += v * level;
    count++;
  });

  return ans;
}
