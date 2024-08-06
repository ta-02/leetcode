function minimumPushes(word: string): number {
  const countMap = word.split("").reduce((map, x) => {
    map.set(x, (map.get(x) || 0) + 1);
    return map;
  }, new Map<string, number>());

  const sortedValues = [...countMap.values()].sort((a, b) => b - a);

  return sortedValues.reduce((ans, v, index) => {
    return ans + v * (Math.floor(index / 8) + 1);
  }, 0);
}
