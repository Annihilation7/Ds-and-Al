# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2020-02-11 10:03pm


class BiPartitionDetection:
    def __init__(self, graph):
        """
        检查图片是否是一个而分图。
        不说定义了，联想一下全连接层就完事了。
        :param graph:
        """
        self.graph = graph

        self.colors = [-1 for _ in range(self.graph.V)]
        self.bipartite_flag = True
        for v in range(self.graph.V):  # 考虑连通分量不只一个的情形
            if self.colors[v] == -1:  # 没被染过色
                # 初始染成0，染成1也一样，无所谓这个
                self.bipartite_flag = self._dfs(v, 0)
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
    def _dfs(self, v, color):
        """dfs，O(V+E)"""
        self.colors[v] = color
        for w in self.graph.adjacent(v):
            if self.colors[w] == -1:
                if not self._dfs(w, 1 - color):  # 相邻节点换颜色
                    return False
            else:  # 已经遍历过了，那就检查一下
                if self.colors[w] == self.colors[v]:
                    return False
        return True