class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isbst(root,maxi,mini):
            if not root:
                return True
            if root.val<mini or root.val>maxi:
                return False
            return isbst(root.left,root.val-1,mini) and isbst(root.right,maxi,root.val+1)
        return isbst(root,float('inf'),float('-inf'))
