class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root,count):
            if not root:
                return 0
            left=height(root.left,count)
            right=height(root.right,count)
            if abs(left-right)>1:
                count[0]=0
            return 1+max(left,right)
        count=[1]
        height(root,count)
        return count[0]
