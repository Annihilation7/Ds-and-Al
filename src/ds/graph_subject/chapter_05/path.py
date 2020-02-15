# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2020-02-15 04:03pm


import queue


class Path:
    def __init__(self, graph, s, t):
        """
        获取图中从源s到t的路径（直接就指定了源和目标）
        可以提前终止bfs，加速运算过程
        :param graph: 传入的图
        :param s: 传入的源
        :param t: 传入的目标节点
        """
        self.graph = graph
        self.graph.validate_vertex(s)
        self.graph.validate_vertex(t)
        self.s = s
        self.t = t

        self.pre = [-1 for _ in range(self.graph.V)]
        self._bfs()

    def is_connected(self):
        """查看传入的s和t是否是相连的"""
        return self.pre[self.t] != -1

    @property
    def path(self):
        """给出从源s到t的路径，不存在则返回空list"""
        ret_path = []
        if not self.is_connected():
            return ret_path
        t_copy = self.t
        while self.pre[t_copy] != t_copy:
            ret_path.append(t_copy)
            t_copy = self.pre[t_copy]
        ret_path.append(t_copy)
        return ret_path[::-1]

    # private
    def _bfs(self):
        """
        没有参数的原因是默认从self.s开始广度优先遍历了
        bfs，O(V+E)
        """
        q = queue.Queue()
        q.put(self.s)
        self.pre[self.s] = self.s  # 源的pre就是自己

        # 提前返回条件1
        if self.s == self.t:
            return

        while not q.empty():
            head = q.get()
            for w in self.graph.adjacent(head):
                if self.pre[w] == -1:
                    q.put(w)
                    self.pre[w] = head
                    # 提前返回条件2
                    if w == self.t:
                        return