from collections import deque


# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        # If root is None, return an empty list
        if root is None:
            return []

        q = deque()
        q.append(root)
        depth = 1
        while q:
            size = len(q)
            level = []
            for _ in range(size):
                cur = q.popleft()
                print(f"当前节点的值为:{cur.val},深度为:{depth}")
                level.append(cur.val)
                for child in cur.children:
                    q.append(child)
            depth += 1


# Example to test the solution
if __name__ == "__main__":
    # Create a sample N-ary tree
    #        1
    #      / | \
    #     3  2  4
    #    / \
    #   5   6

    node5 = Node(5)
    node6 = Node(6)
    node3 = Node(3, [node5, node6])
    node2 = Node(2)
    node4 = Node(4)
    root = Node(1, [node3, node2, node4])

    solution = Solution()
    solution.levelOrder(root)

