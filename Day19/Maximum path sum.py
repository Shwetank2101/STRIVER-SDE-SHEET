class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def pathsum(root,ans):
            if not root:
                return 0
            l=pathsum(root.left,ans)
            r=pathsum(root.right,ans)
            m=max(max(l,r)+root.val,root.val)
            ans[0]=max(m,ans[0],l+r+root.val)
            return m
        ans=[-1000000]
        pathsum(root,ans)
        return ans[0]
