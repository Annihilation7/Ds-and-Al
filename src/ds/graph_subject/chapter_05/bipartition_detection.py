# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2020-02-15 05:35pm


import queue


class BiPartitionDetection:
    def __init__(self, graph):
        """
        检查图片是否是一个二分图。
        不说定义了，联想一下全连接层就完事了。
        :param graph:
        """
        self.graph = graph

        self.colors = [-1 for _ in range(self.graph.V)]
        self.bipartite_flag = True
        for v in range(self.graph.V):  # 考虑连通分量不只一个的情形
            if self.colors[v] == -1:  # 没被染过色
                # 初始染成0，染成1也一样，无所谓这个
                self.bipartite_flag = self._bfs(v)
                if not self.bipartite_flag:  # 提前结束
                    break

    def is_bipartite(self):
        """返回是否是一个二分图"""
        return self.bipartite_flag

    def get_patrition_vertexes(self):
        """返回二分图的顶点划分数组"""
        if not self.bipartite_flag:
            return []  # 返回空数组表明传入的图不是一个二分图

        res = [[] for _ in range(2)]
        for i in range(len(self.colors)):
            res[self.colors[i]].append(i)
        return res

    # private
    def _bfs(self, v):
        """bfs，O(V+E)"""
        q = queue.Queue()
        q.put(v)
        self.colors[v] = 0  # 1也一样，无所谓的

        while not q.empty():
            head = q.get()
            for w in self.graph.adjacent(head):
                if self.colors[w] == -1:  # 没被遍历过
                    q.put(w)
                    self.colors[w] = 1 - self.colors[head]  # 和head反色
                # 被遍历过并且不和head反色，那就返回False
                elif self.colors[w] != 1 - self.colors[head]:
                    return False
        return True