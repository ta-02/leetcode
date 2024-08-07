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

function kthSmallest(root: TreeNode | null, k: number): number {
  let count = 0;
  let res: number | null = null;

  const inOrder = (root: TreeNode | null) => {
    if (!root || res !== null) return;
    inOrder(root.left);
    count++;
    if (count === k) {
      res = root.val;
      return;
    }
    inOrder(root.right);
  };

  inOrder(root);
  return res!;
}
