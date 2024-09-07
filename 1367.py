class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        def check_path(b_node, l_node):
            if not l_node:
                return True
            if not b_node:
                return False

            return b_node.val == l_node.val and (
                check_path(b_node.left, l_node.next)
                or check_path(b_node.right, l_node.next)
            )

        def dfs(b_node):
            if not b_node:
                return False

            return check_path(b_node, head) or dfs(b_node.left) or dfs(b_node.right)

        return dfs(root)
