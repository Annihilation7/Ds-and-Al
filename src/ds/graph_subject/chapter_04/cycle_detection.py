# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2020-02-11 09:02pm


class CycleDetection:
    def __init__(self, graph):
        """
        检测输入的一张图是否存在环
        :param graph: 输入的图
        """
        self.graph = graph

        self.cycle_flag = False
        self.pre = [-1 for _ in range(self.graph.V)]
        for v in range(self.graph.V):  # 考虑连通分量不只一个的情形
            if self.pre[v] == -1:
                self.cycle_flag = self._dfs(v, v)
                if self.cycle_flag:  # 某一个连通分量存在环直接break就完事了
                    break

    def has_cycle(self):
        return self.cycle_flag

    # private
    def _dfs(self, v, s):
        """dfs，O(V+E)"""
        self.pre[v] = s
        for w in self.graph.adjacent(v):
            if self.pre[w] == -1:  # 还没被遍历过
                if self._dfs(w, v):
                    return True
            else:
                # 遍历过了，且父节点不是当前节点的上一个节点，则为有环
                # 这里的逻辑要着重理解一下
                if w != s:
                    return True
        return False
