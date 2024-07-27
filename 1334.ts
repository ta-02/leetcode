function findTheCity(
  n: number,
  edges: number[][],
  distanceThreshold: number,
): number {
  const dist = Array.from({ length: n }, () => Array(n).fill(Infinity));

  for (let i = 0; i < n; i++) {
    dist[i][i] = 0;
  }

  for (const [c, v, w] of edges) {
    dist[c][v] = w;
    dist[v][c] = w;
  }

  for (let k = 0; k < n; k++) {
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
      }
    }
  }

  let city = -1;
  let minReachable = n;
  for (let i = 0; i < n; i++) {
    let reachable = 0;
    for (let j = 0; j < n; j++) {
      if (i !== j && dist[i][j] <= distanceThreshold) {
        reachable++;
      }
    }
    if (reachable <= minReachable) {
      minReachable = reachable;
      city = i;
    }
  }

  return city;
}
