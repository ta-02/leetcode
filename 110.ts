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

function isBalanced(root: TreeNode | null): boolean {
  let isOk = true;

  const dfs = (root: TreeNode | null): number => {
    if (!root) return 0;
    const left = dfs(root.left);
    const right = dfs(root.right);
    const bf = Math.abs(left - right);
    if (bf !== 0 && bf !== 1) isOk = false;
    return Math.max(left, right) + 1;
  };
  dfs(root);
  return isOk;
}
