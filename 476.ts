function findComplement(num: number): number {
  let bnum: number[] = [];
  while (num) {
    bnum.push(num % 2);
    num = Math.floor(num / 2);
  }

  return bnum
    .map((x) => Number(!x))
    .reduce((t, x, i) => t + x * Math.pow(2, i + 1), 0);
}
