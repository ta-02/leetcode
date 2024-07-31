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

function rightSideView(root: TreeNode | null): number[] {
  const ans = [];
  const helper = (root: TreeNode | null, i: number) => {
    if (!root) return;
    if (ans[i] === undefined) ans.push(root.val);
    helper(root.right, i + 1);
    helper(root.left, i + 1);
  };
  helper(root, 0);
  return ans;
};
