# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2020-02-08 06:32pm


import abc


class GraphBase(metaclass=abc.ABCMeta):

    def print(self):
        """打印图的成员函数"""
        pass

    @property
    def V(self):
        """返回Vertex的数量"""
        pass

    @property
    def E(self):
        """返回Edge的数量"""
        pass

    def has_edge(self, v, w):
        """判断两个Vertex之间是否存在边"""
        pass

    def adjacent(self, v):
        """
        拿到所有与输入Vertex相邻的Vertex index
        """
        pass

    def degree(self, v):
        """拿到输入Vertex的边的数量"""
        pass

    # private
    def _build_graph(self, filepath):
        pass

    def _validate_vertex(self, v):
        """检查节点index的合法性"""
        assert 0 <= v < self.V, 'Invalid vertex idx: {}'.format(v)
