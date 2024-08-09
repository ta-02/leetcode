function numMagicSquaresInside(grid: number[][]): number {
  let count = 0;
  for (let i = 0; i < grid.length - 2; i++) {
    for (let j = 0; j < grid[0].length - 2; j++) {
      if (isMagicSquare(grid, i, j)) {
        count++;
      }
    }
  }
  return count;
}

function isMagicSquare(
  grid: number[][],
  startR: number,
  startC: number,
): boolean {
  const seenNums = new Set<number>();

  const targetSum =
    grid[startR][startC] + grid[startR][startC + 1] + grid[startR][startC + 2];

  for (let i = 0; i < 3; i++) {
    let rowSum = 0;
    for (let j = 0; j < 3; j++) {
      const num = grid[startR + i][startC + j];
      if (num < 1 || num > 9 || seenNums.has(num)) {
        return false;
      }
      seenNums.add(num);
      rowSum += num;
    }
    if (rowSum !== targetSum) {
      return false;
    }
  }

  for (let j = 0; j < 3; j++) {
    let colSum = 0;
    for (let i = 0; i < 3; i++) {
      colSum += grid[startR + i][startC + j];
    }
    if (colSum !== targetSum) {
      return false;
    }
  }

  const diagonal1Sum =
    grid[startR][startC] +
    grid[startR + 1][startC + 1] +
    grid[startR + 2][startC + 2];
  const diagonal2Sum =
    grid[startR][startC + 2] +
    grid[startR + 1][startC + 1] +
    grid[startR + 2][startC];

  if (diagonal1Sum !== targetSum || diagonal2Sum !== targetSum) {
    return false;
  }

  return true;
}
