# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2020-02-15 02:38pm


import queue


class GraphBfs:
    def __init__(self, graph):
        """
        图的广度优先遍历类，和二分搜索树的广度优先遍历差不多，区别就是多个了节点记录功能
        :param graph: 传入的图
        """
        self.graph = graph

        self.visited = [False] * self.graph.V
        self.bfs_order = []

        for v in range(self.graph.V):  # 考虑连通分量不只一个的情形
            if not self.visited[v]:
                self._bfs(v)

    def get_bfs_order(self):
        return self.bfs_order

    # private
    def _bfs(self, v):
        """bfs，O(V+E)"""
        q = queue.Queue()
        q.put(v)
        self.visited[v] = True

        while not q.empty():
            head = q.get()
            self.bfs_order.append(head)
            for w in self.graph.adjacent(head):
                if not self.visited[w]:
                    q.put(w)
                    self.visited[w] = True