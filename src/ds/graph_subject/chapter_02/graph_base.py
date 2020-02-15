# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2020-02-08 06:32pm


import abc


class GraphBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def print(self):
        """打印图的成员函数"""
        pass

    @property
    @abc.abstractmethod
    def V(self):
        """返回Vertex的数量"""
        pass

    @property
    @abc.abstractmethod
    def E(self):
        """返回Edge的数量"""
        pass

    @abc.abstractmethod
    def has_edge(self, v, w):
        """判断两个Vertex之间是否存在边"""
        pass

    @abc.abstractmethod
    def adjacent(self, v):
        """
        拿到所有与输入Vertex相邻的Vertex index
        """
        pass

    @abc.abstractmethod
    def degree(self, v):
        """拿到输入Vertex的边的数量"""
        pass

    def validate_vertex(self, v):
        """检查节点index的合法性"""
        assert 0 <= v < self.V, 'Invalid vertex idx: {}'.format(v)

    # private
    @abc.abstractmethod
    def _build_graph(self, filepath):
        pass
