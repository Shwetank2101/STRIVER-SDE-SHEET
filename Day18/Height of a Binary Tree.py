class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def height(root):
            if not root:
                return 0
            left=height(root.left)
            right=height(root.right)
            if left>right:
                return left+1
            else:
                return right+1
        return height(root)
