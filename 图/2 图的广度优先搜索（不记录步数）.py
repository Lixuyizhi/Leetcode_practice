# 多叉树的层序遍历
def levelOrderTraverse(root):
    if root is None:
        return
    from collections import deque
    q = deque([root])
    while q:
        cur = q.popleft()
        # 访问 cur 节点
        print(cur.val)

        # 把 cur 的所有子节点加入队列
        for child in cur.children:
            q.append(child)

# 图结构的 BFS 遍历，从节点 s 开始进行 BFS
def bfs(graph, s):
    visited = [False] * len(graph)
    from collections import deque
    q = deque([s])
    visited[s] = True

    while q:
        cur = q.popleft()
        print(f"visit {cur}")
        for e in graph.neighbors(cur):
            if not visited[e.to]:
                q.append(e.to)
                visited[e.to] = True