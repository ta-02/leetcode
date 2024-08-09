function numMagicSquaresInside(grid: number[][]): number {
  let count = 0;

  for (let i = 0; i <= grid.length - 3; i++) {
    for (let j = 0; j <= grid[0].length - 3; j++) {
      const subgrid = [
        [grid[i][j], grid[i][j + 1], grid[i][j + 2]],
        [grid[i + 1][j], grid[i + 1][j + 1], grid[i + 1][j + 2]],
        [grid[i + 2][j], grid[i + 2][j + 1], grid[i + 2][j + 2]],
      ];
      if (isMagicSquare(subgrid)) {
        count++;
      }
    }
  }

  return count;
}

function isMagicSquare(grid: number[][]): boolean {
  const seenNumbers = new Set<number>();
  for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
      const num = grid[i][j];
      if (num < 1 || num > 9 || seenNumbers.has(num)) {
        return false;
      }
      seenNumbers.add(num);
    }
  }

  const targetSum = grid[0][0] + grid[0][1] + grid[0][2];

  for (let i = 0; i < 3; i++) {
    const rowSum = grid[i][0] + grid[i][1] + grid[i][2];
    if (rowSum !== targetSum) {
      return false;
    }
  }

  for (let j = 0; j < 3; j++) {
    const colSum = grid[0][j] + grid[1][j] + grid[2][j];
    if (colSum !== targetSum) {
      return false;
    }
  }

  const diagonal1Sum = grid[0][0] + grid[1][1] + grid[2][2];
  const diagonal2Sum = grid[0][2] + grid[1][1] + grid[2][0];
  if (diagonal1Sum !== targetSum || diagonal2Sum !== targetSum) {
    return false;
  }

  return true;
}
