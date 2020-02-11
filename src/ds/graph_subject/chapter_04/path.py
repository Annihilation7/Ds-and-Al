# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2020-02-11 08:33pm


class Path:
    def __init__(self, graph, s, t):
        """
        获取图中从源s到t的路径（直接就指定了源和目标）
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
        self.connected = self._dfs(s, s)  # 只需从源开始dfs就完事了

    def is_connected(self):
        """查看传入的s和t是否是相连的"""
        return self.pre[self.t] != -1  # 看遍没遍历过就完事了

    @property
    def path(self):
        """给出从源s到t的路径，不存在则返回空list"""
        ret_path = []
        if not self.is_connected():  # 根本就不可达，返回空list
            return ret_path
        # 就是一个简单的并查集find方法
        t_copy = self.t
        while self.pre[t_copy] != t_copy:
            ret_path.append(t_copy)
            t_copy = self.pre[t_copy]
        ret_path.append(t_copy)  # 最后安排一下源
        # 此时源在ret_path最右侧，路径的方向反人类，反转一下就好
        return ret_path[::-1]

    # private
    def _dfs(self, v, v_source):
        """
        dfs，O(V+E)
        :param v: 当前的节点
        :param v_source: 当前节点的源
        :return: 若存在从s到t的路径，则返回True，否则返回False
        """
        self.pre[v] = v_source  # 类似和并查集，从孩子指向父亲的一颗多叉树
        if v == self.t:  # 找到了，立刻返回
            return True
        for w in self.graph.adjacent(v):
            if self.pre[w] == -1:  # 还没被dfs污染过
                if self._dfs(w, v):
                    return True  # adjcent(v)中存在路径则也直接返回True
        return False