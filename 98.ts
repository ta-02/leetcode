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

function isValidBST(root: TreeNode | null): boolean {
  const helper = (node: TreeNode | null, lower: number, higher: number) => {
    if (!node) return true;

    if (node.val <= lower || node.val >= higher) return false;

    return (
      true &&
      helper(node.left, lower, node.val) &&
      helper(node.right, node.val, higher)
    );
  };
  return helper(root, -Infinity, Infinity);
}
