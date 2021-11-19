# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
       self.res=[]
    def inorderTraversal(self, root) :
        if root is None:
            return []
        else:
            self.inorderTraversal(root.left)
            self.res.append(root.val)
            self.inorderTraversal(root.right)
        return self.res

n1=TreeNode(2)
n2=TreeNode(1)
n3=TreeNode(3)

n1.left=n2
n1.right=n3

sol=Solution()
result=sol.inorderTraversal(n1)

print(f"{result}")
print(f"{sol.res}")