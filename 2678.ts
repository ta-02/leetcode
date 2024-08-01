function countSeniors(details: string[]): number {
  let ans = 0;
  details.forEach((x) => {
    if (+x.slice(11, 13) > 60) ans++;
  });
  return ans;
}
