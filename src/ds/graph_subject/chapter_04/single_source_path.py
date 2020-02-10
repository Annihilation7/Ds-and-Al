# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2020-02-12 12:35am


class SingleSourcePath:
    def __init__(self, graph, s):
        """
        图单源路径的构造函数
        :param graph: 传入的图
        :param s: 传入的源
        """
        self.graph = graph
        self.graph.validate_vertex(s)
        self.s = s

        # pre中每个索引上的值有两个含义：
        # 1。每个节点的父亲节点
        # 2。如果值为默认值-1，则代表没有遍历过，
        # 因为节点的值的值域为[0, self.graph.V-1]，依据这个条件，我们就
        # 可以拿掉visited数组了，节省了O(V)的空间。
        self.pre = [-1 for _ in range(self.graph.V)]
        self._dfs(s, s)  # 只需从源开始dfs就完事了

    def is_connected_to(self, t):
        """从传入的源到某一个节点t是否是可达到的"""
        self.graph.validate_vertex(t)
        return self.pre[t] != -1  # 看遍没遍历过就完事了

    def path(self, t):
        """计算从源到节点t的一条路径，注意不一定是最短路径"""
        self.graph.validate_vertex(t)
        ret_path = []
        if not self.is_connected_to(t):  # 根本就不可达，返回空list
            return ret_path
        # 就是一个简单的并查集find方法
        while self.pre[t] != t:
            ret_path.append(t)
            t = self.pre[t]
        ret_path.append(t)  # 最后安排一下源
        # 此时源在ret_path最右侧，路径的方向反人类，反转一下就好
        return ret_path[::-1]

    # private
    def _dfs(self, v, v_source):
        """
        dfs，O(V+E)
        :param v: 当前的节点
        :param v_source: 当前节点的源
        """
        self.pre[v] = v_source  # 类似和并查集，从孩子指向父亲的一颗多叉树
        for w in self.graph.adjacent(v):
            if self.pre[w] == -1:  # 还没被dfs污染过
                self._dfs(w, v)
