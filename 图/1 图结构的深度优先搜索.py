# 多叉树节点
class Node:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children if children is not None else []

# 多叉树的遍历框架
def traverse(root):
    # base case
    if root is None:
        return
    # 前序位置
    print(f"visit {root.val}")
    for child in root.children:
        traverse(child)
    # 后序位置

# 图节点
class Vertex:
    def __init__(self, id=0, neighbors=None):
        self.id = id
        self.neighbors = neighbors if neighbors is not None else []

# 图的遍历框架
# 需要一个 visited 数组记录被遍历过的节点
# 避免走回头路陷入死循环
def traverse_graph(s, visited):
    # base case
    if s is None:
        return
    if visited[s]:
        # 防止死循环
        return
    # 前序位置
    visited[s] = True
    print(f"visit {s.id}")
    for neighbor in s.neighbors:
        traverse_graph(neighbor, visited)
    # 后序位置