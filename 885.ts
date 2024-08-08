function spiralMatrixIII(
  rows: number,
  cols: number,
  rStart: number,
  cStart: number,
): number[][] {
  const directions: number[][] = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
  ];
  const res: number[][] = [];
  let r = rStart,
    c = cStart;
  let steps = 1;
  let i = 0;

  while (res.length < rows * cols) {
    for (let x = 0; x < 2; x++) {
      const [dr, dc] = directions[i];
      for (let y = 0; y < steps; y++) {
        if (0 <= r && r < rows && 0 <= c && c < cols) {
          res.push([r, c]);
        }
        r += dr;
        c += dc;
      }
      i = (i + 1) % 4;
    }
    steps += 1;
  }

  return res;
}
