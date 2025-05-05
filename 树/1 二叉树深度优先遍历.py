# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        d = []
        traverse(root, d)  # 直接调用全局函数 traverse
        return d

def traverse(root, l):
    if root is None:
        return
    # 前序位置
    l.append(root.val)
    traverse(root.left, l)  # 递归调用全局函数
    # 中序位置
    traverse(root.right, l)  # 递归调用全局函数
    # 后序位置

# 创建一个二叉树作为实例
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

solution = Solution()
print(solution.preorderTraversal(root))

