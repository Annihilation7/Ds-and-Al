# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2020-02-10 01:38am


class GraphDfs:
    def __init__(self, graph):
        self.graph = graph

        self.visited = [False] * self.graph.V
        self.pre = []  # 存先序遍历的结果
        self.post = []  # 存后序遍历的结果
        for v in range(self.graph.V):  # 考虑连通分量不只一个的情形
            if not self.visited[v]:
                self._dfs(v)

    def get_pre_order(self):
        return self.pre

    def get_post_order(self):
        return self.post

    # private
    def _dfs(self, v):
        """dfs，O(V+E)"""
        self.pre.append(v)  # 先序
        self.visited[v] = True
        for w in self.graph.adjacent(v):
            if not self.visited[w]:
                self._dfs(w)
        self.post.append(v)  # 后序
