# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2020-02-15 06:10pm


import queue


# Unweighted Single Source Shortest Path
class USSSPath:
    def __init__(self, graph, s):
        """
        基于图的广度优先遍历求解到某一个源的最短路径问题
        注意基于广度优先遍历求最短路径的算法只适用于无权图的最短路径问题的求解
        :param graph: 传入的图
        :param s: 传入的源
        """
        self.graph = graph
        self.graph.validate_vertex(s)
        self.s = s

        self.pre = [-1 for _ in range(self.graph.V)]
        # 多了一个代表每个节点到源的距离的辅助数组
        self.dst = [-1 for _ in range(self.graph.V)]
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

    def get_distance(self, v):
        """
        求传入的节点到源点的距离
        返回-1代表该点并不在以self.s为源的连通分量中
        """
        self.graph.validate_vertex(v)
        return self.dst[v]

    # private
    def _bfs(self, v):
        """bfs，O(V+E)"""
        q = queue.Queue()
        q.put(v)
        self.pre[v] = v  # 源的pre就是自己
        self.dst[v] = 0  # 记录自己到自己的距离，就是0

        while not q.empty():
            head = q.get()
            for w in self.graph.adjacent(head):
                if self.pre[w] == -1:
                    q.put(w)
                    self.pre[w] = head
                    self.dst[w] = self.dst[head] + 1  # 下一层，深度加一，很简单
