function sortArray(nums: number[]): number[] {
  const MergeSort = (nums: number[]) => {
    if (nums.length <= 1) return nums;
    const halfLen = Math.floor(nums.length / 2);
    const h1 = MergeSort(nums.slice(0, halfLen));
    const h2 = MergeSort(nums.slice(halfLen));
    const mergedArray: number[] = [];
    let i1 = 0,
      i2 = 0;
    while (i1 < h1.length && i2 < h2.length) {
      if (h1[i1] < h2[i2]) {
        mergedArray.push(h1[i1++]);
      } else {
        mergedArray.push(h2[i2++]);
      }
    }
    mergedArray.push(...h1.slice(i1));
    mergedArray.push(...h2.slice(i2));
    return mergedArray;
  };
  return MergeSort(nums);
}
