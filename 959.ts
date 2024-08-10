function regionsBySlashes(grid: string[]): number {
  const n = grid.length;
  const upscaleSize = n * 3;
  const g = Array.from({ length: upscaleSize }, () =>
    Array(upscaleSize).fill(0),
  );

  for (let i = 0; i < n; ++i) {
    for (let j = 0; j < n; ++j) {
      if (grid[i][j] === "/") {
        g[i * 3][j * 3 + 2] = 1;
        g[i * 3 + 1][j * 3 + 1] = 1;
        g[i * 3 + 2][j * 3] = 1;
      } else if (grid[i][j] === "\\") {
        g[i * 3][j * 3] = 1;
        g[i * 3 + 1][j * 3 + 1] = 1;
        g[i * 3 + 2][j * 3 + 2] = 1;
      }
    }
  }

  const directions: number[][] = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ];

  const dfs = (startI: number, startJ: number): void => {
    const stack: number[][] = [];
    stack.push([startI, startJ]);

    while (stack.length) {
      const [i, j] = stack.pop()!;

      g[i][j] = 1;

      directions.forEach(([di, dj]) => {
        const newI = i + di;
        const newJ = j + dj;
        if (
          newI >= 0 &&
          newI < upscaleSize &&
          newJ >= 0 &&
          newJ < upscaleSize &&
          g[newI][newJ] === 0
        ) {
          stack.push([newI, newJ]);
        }
      });
    }
  };

  let regions = 0;

  for (let i = 0; i < upscaleSize; ++i) {
    for (let j = 0; j < upscaleSize; ++j) {
      if (g[i][j] === 0) {
        dfs(i, j);
        regions++;
      }
    }
  }

  return regions;
}
