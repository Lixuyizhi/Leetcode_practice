# 多叉树的层序遍历
# 每个节点自行维护 State 类，记录深度等信息
class State:
    def __init__(self, node, depth):
        self.node = node
        self.depth = depth


def levelOrderTraverse(root):
    if root is None:
        return
    from collections import deque
    q = deque([State(root, 1)])
    while q:
        state = q.popleft()
        cur = state.node
        depth = state.depth
        # 访问 cur 节点，同时知道它所在的层数
        print(f"depth = {depth}, val = {cur.val}")

        for child in cur.children:
            q.append(State(child, depth + 1))


# 图结构的 BFS 遍历，从节点 s 开始进行 BFS，且记录路径的权重和
# 每个节点自行维护 State 类，记录从 s 走来的权重和
class State:
    def __init__(self, node, weight):
        # 当前节点 ID
        self.node = node
        # 从起点 s 到当前节点的权重和
        self.weight = weight


def bfs(graph, s):
    visited = [False] * len(graph)
    from collections import deque

    q = deque([State(s, 0)])
    visited[s] = True

    while q:
        state = q.popleft()
        cur = state.node
        weight = state.weight
        print(f"visit {cur} with path weight {weight}")
        for e in graph.neighbors(cur):
            if not visited[e.to]:
                q.append(State(e.to, weight + e.weight))
                visited[e.to] = True