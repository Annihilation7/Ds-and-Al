# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2020-02-11 11:24pm


class CC:
    def __init__(self, graph):
        self.graph = graph
        self.cc_count = 0

        self.visited = [-1] * self.graph.V  # 初始化-1表示节点没被遍历过
        for v in range(self.graph.V):  # 考虑连通分量不只一个的情形
            if self.visited[v] == -1:
                self._dfs(v, self.cc_count)
                self.cc_count += 1

    @property
    def cccount(self):
        """返回连通分量的个数"""
        return self.cc_count

    def is_connected(self, v, w):
        """判断两个节点是否同属于一个联通分量"""
        self.graph.validate_vertex(v)
        self.graph.validate_vertex(w)
        return self.visited[v] == self.visited[w]

    @property
    def components(self):
        """更加直观的拿到全部连通分量"""
        res = [[] for _ in range(self.cc_count)]  # 长度为连通分量的个数
        for cc_idx in range(len(self.visited)):
            res[self.visited[cc_idx]].append(cc_idx)
        return res

    # private
    def _dfs(self, v, cc_idx):
        """dfs，O(V+E)"""
        self.visited[v] = cc_idx
        for w in self.graph.adjacent(v):
            if self.visited[w] == -1:
                self._dfs(w, cc_idx)
