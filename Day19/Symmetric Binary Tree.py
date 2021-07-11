class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(a,b):
            if not a and not b:
                return True
            if a and b and a.val==b.val:
                return (check(a.left,b.right) and check(a.right,b.left))
            return False
        return check(root,root)
