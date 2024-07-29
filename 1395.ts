function numTeams(rating: number[]): number {
  let ans = 0;
  const n = rating.length;

  for (let i = 0; i < n; i++) {
    let smallerLeft = 0,
      greaterLeft = 0;

    for (let j = 0; j < i; j++) {
      if (rating[i] < rating[j]) greaterLeft++;
      if (rating[i] > rating[j]) smallerLeft++;
    }

    let smallerRight = 0,
      greaterRight = 0;

    for (let j = i + 1; j < n; j++) {
      if (rating[i] < rating[j]) greaterRight++;
      if (rating[i] > rating[j]) smallerRight++;
    }

    ans += smallerLeft * greaterRight + greaterLeft * smallerRight;
  }

  return ans;
}
