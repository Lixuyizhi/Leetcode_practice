from collections import deque


# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

# Definition for a State
class State(object):
    def __init__(self,node,weigh):
        self.node = node
        self.weigh = weigh

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        # If root is None, return an empty list
        if root is None:
            return []

        depth = 1
        q = deque()
        q.append(State(root,depth))
        while q:
            size = len(q)
            for _ in range(size):
                cur = q.popleft()
                print(f"当前节点的值为:{cur.node.val},权重为:{cur.weigh}")
                for child in cur.node.children:
                    q.append(State(child,depth+1))
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

