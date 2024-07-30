function minimumDeletions(s: string): number {
  let leftB = 0;
  let rightA = s.split("a").length - 1;
  let best = rightA;

  s.split("").forEach((x) => {
    x === "b" ? leftB++ : rightA--;
    best = Math.min(best, leftB + rightA);
  });

  return best;
}
