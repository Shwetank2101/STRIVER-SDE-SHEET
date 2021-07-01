class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None
        q=[root]
        res=[]
        while q:
            level=[]
            for i in range(len(q)):
                x=q.pop(0)
                level.append(x.val)
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
            res.append(level[0])
        return res
