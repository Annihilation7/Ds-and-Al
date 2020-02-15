# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2020-02-15 05:01pm


import queue


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
                self.cycle_flag = self._bfs(v)
                if self.cycle_flag:  # 某一个连通分量存在环直接break就完事了
                    break

    def has_cycle(self):
        return self.cycle_flag

    # private
    def _bfs(self, v):
        """bfs，O(V+E)"""
        q = queue.Queue()
        q.put(v)
        self.pre[v] = v

        while not q.empty():
            head = q.get()
            for w in self.graph.adjacent(head):
                if self.pre[w] == -1:
                    q.put(w)
                    self.pre[w] = head
                # 已经被遍历过，但w不是head的父亲节点，此时表明有环
                elif self.pre[head] != w:
                    return True
        return False