class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def height(root, ans):
            if not root:
                return 0
            left=height(root.left,ans)
            right=height(root.right,ans)
            ans[0]=max(ans[0],left+right)
            return 1+max(left,right)
        ans=[0]
        height(root,ans)
        return ans[0]
