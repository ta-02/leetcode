function secondHighest(s: string): number {
  return (
    Array.from(
      s.split("").reduce((set, x) => {
        if ("0" <= x && x <= "9") set.add(+x);
        return set;
      }, new Set<number>()),
    ).sort((a, b) => b - a)[1] ?? -1
  );
}
