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

function levelOrder(root: TreeNode | null): number[][] {
  const ans: number[][] = [];

  const helper = (node: TreeNode | null, level: number) => {
    if (!node) return;

    if (ans.length === level) {
      ans.push([]);
    }

    ans[level].push(node.val);
    helper(node.left, level + 1);
    helper(node.right, level + 1);
  }

  helper(root, 0);
  return ans;
}
