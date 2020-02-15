# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2020-02-15 03:42pm


import queue


class SingleSourcePath:
    def __init__(self, graph, s):
        """
        基于图的广度优先遍历求解单源路径问题
        :param graph: 传入的图
        :param s: 传入的源
        """
        self.graph = graph
        self.graph.validate_vertex(s)
        self.s = s

        self.pre = [-1 for _ in range(self.graph.V)]
        self._bfs(s)

    def is_connected_to(self, v):
        """查看某一节点是否和当前的源是连同的"""
        self.graph.validate_vertex(v)
        return self.pre[v] != -1

    def path(self, v):
        """获取当前的源到节点v的一条路径"""
        self.graph.validate_vertex(v)

        ret_path = []
        if not self.is_connected_to(v):
            return ret_path
        while self.pre[v] != v:
            ret_path.append(v)
            v = self.pre[v]
        ret_path.append(v)
        return ret_path[::-1]

    # private
    def _bfs(self, v):
        """bfs，O(V+E)"""
        q = queue.Queue()
        q.put(v)
        self.pre[v] = v  # 源的pre就是自己

        while not q.empty():
            head = q.get()
            for w in self.graph.adjacent(head):
                if self.pre[w] == -1:
                    q.put(w)
                    self.pre[w] = head