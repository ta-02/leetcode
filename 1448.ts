class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

function goodNodes(root: TreeNode | null): number {
  let ans = 0;

  const helper = (root: TreeNode | null, maxValue: number) => {
    if (!root) return;
    if (root.val >= maxValue) {
      maxValue = root.val;
      ans++;
    }
    helper(root.left, maxValue);
    helper(root.right, maxValue);
  };

  helper(root, -Infinity);
  return ans;
}
