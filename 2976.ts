function minimumCost(
  source: string,
  target: string,
  original: string[],
  changed: string[],
  cost: number[],
): number {
  const CODE_A = "a".charCodeAt(0);
  const N = 26;
  const n = source.length;
  const costMatrix = Array.from({ length: N }, () => Array(N).fill(Infinity));

  for (let i = 0; i < N; i++) {
    costMatrix[i][i] = 0;
  }

  for (let i = 0; i < original.length; i++) {
    const from = original[i].charCodeAt(0) - CODE_A;
    const to = changed[i].charCodeAt(0) - CODE_A;
    costMatrix[from][to] = Math.min(cost[i], costMatrix[from][to]);
  }

  for (let k = 0; k < N; k++) {
    for (let i = 0; i < N; i++) {
      for (let j = 0; j < N; j++) {
        costMatrix[i][j] = Math.min(
          costMatrix[i][j],
          costMatrix[i][k] + costMatrix[k][j],
        );
      }
    }
  }

  let minCost = 0;
  for (let i = 0; i < n; i++) {
    const from = source[i].charCodeAt(0) - CODE_A;
    const to = target[i].charCodeAt(0) - CODE_A;
    minCost += costMatrix[from][to];
  }
  return isFinite(minCost) ? minCost : -1;
}
