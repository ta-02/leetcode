function minHeightShelves(books: number[][], shelfWidth: number): number {
  const cache = new Map<number, number>();

  const helper = (i: number): number => {
    if (i === books.length) return 0;

    if (cache.has(i)) {
      return cache.get(i)!;
    }

    let currWidth = shelfWidth;
    let maxHeight = 0;
    let minHeight = Infinity;

    for (let j = i; j < books.length; j++) {
      const [width, height] = books[j];
      if (width > currWidth) break;
      currWidth -= width;
      maxHeight = Math.max(maxHeight, height);
      minHeight = Math.min(minHeight, helper(j + 1) + maxHeight);
    }

    cache.set(i, minHeight);
    return minHeight;
  };

  return helper(0);
}
