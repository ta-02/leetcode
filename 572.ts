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

const isSameTree = (
  root: TreeNode | null,
  subRoot: TreeNode | null
): boolean => {
  if (!root && !subRoot) return true;
  if (!root || !subRoot) return false;
  if (root.val !== subRoot.val) return false;
  return (
    isSameTree(root.left, subRoot.left) && isSameTree(root.right, subRoot.right)
  );
};

function isSubtree(root: TreeNode | null, subRoot: TreeNode | null): boolean {
  if (!subRoot) return true;
  if (!root) return false;
  return (
    isSameTree(root, subRoot) ||
    isSubtree(root.left, subRoot) ||
    isSubtree(root.right, subRoot)
  );
}
