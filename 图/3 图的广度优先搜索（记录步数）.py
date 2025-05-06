from collections import deque


# 多叉树的层序遍历
def levelOrderTraverse(root):
    if root is None:
        return
    q = deque([root])
    # 记录当前遍历到的层数（根节点视为第 1 层）
    depth = 1

    while q:
        sz = len(q)
        for _ in range(sz):
            cur = q.popleft()
            # 访问 cur 节点，同时知道它所在的层数
            print(f"depth = {depth}, val = {cur.val}")

            for child in cur.children:
                q.append(child)
        depth += 1


# 从 s 开始 BFS 遍历图的所有节点，且记录遍历的步数
def bfs(graph, s):
    visited = [False] * len(graph)
    q = deque([s])
    visited[s] = True
    # 记录从 s 开始走到当前节点的步数
    step = 0

    while q:
        sz = len(q)
        for i in range(sz):
            cur = q.popleft()
            print(f"visit {cur} at step {step}")
            for e in graph.neighbors(cur):
                if not visited[e.to]:
                    q.append(e.to)
                    visited[e.to] = True
        step += 1