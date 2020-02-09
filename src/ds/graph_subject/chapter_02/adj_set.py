# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2020-02-08 06:13pm


from src.ds.avl_tree import AvlTree
from src.ds.graph_subject.chapter_02.graph_base import GraphBase


class AdjSet(GraphBase):
    """
    图的"邻接表(AvlTree)"表示法。建图空间复杂度为O(Elog(V))，时间复杂度为O(E*V)
    我这里采取Avl数来代替红黑树了，因为红黑树中并没有实现删除元素的操作。
    """
    def __init__(self, filepath):
        self._build_graph(filepath)

    def __str__(self):
        return 'AdjSet'

    def print(self):
        """打印邻接表的成员函数"""
        print('V = {}, E = {}'.format(self.V, self.E))
        for i in range(self.V):
            print('{} :'.format(i), self.adj[i].print_in_adj_set())

    def V(self):
        """返回Vertex的数量"""
        return self.V

    def E(self):
        """返回Edge的数量"""
        return self.E

    def has_edge(self, v, w):
        """判断两个Vertex之间是否存在边，O(logV)"""
        self._validate_vertex(v)
        self._validate_vertex(w)
        return self.adj[v].contains(w)

    def adjacent(self, v):
        """拿到所有与输入Vertex相邻的Vertex，直接返回所对avl数的根节点，O(degree(V))"""
        self._validate_vertex(v)
        return self.adj[v]

    def degree(self, v):
        """拿到输入Vertex的边的数量"""
        return self.adjacent(v).getSize()

    # private
    def _build_graph(self, filepath):
        first_line_flag = True
        with open(filepath, 'r', encoding='utf-8') as fp:
            try:
                while True:
                    line = fp.readline()
                    if first_line_flag:
                        elem1, elem2 = self._valid_check_parse(
                            line, first_line_flag
                        )
                        self.V, self.E = elem1, elem2
                        # 邻接表其实就是数组套链表的结构
                        self.adj = [AvlTree() for _ in range(self.V)]
                        first_line_flag = False
                    else:
                        elem1, elem2 = self._valid_check_parse(
                            line, first_line_flag
                        )
                        # 注意是无向图
                        self.adj[elem1].add(elem2)  # O(logV)
                        self.adj[elem2].add(elem1)
            except ValueError:
                print('Input file has been parsed successfully.')

    def _valid_check_parse(self, line, first_line_flag):
        """解析一行数据，并包含必要的有效判断"""
        parse_line = lambda line: (int(elem) for elem in line.split(' '))
        try:
            elem1, elem2 = parse_line(line)
            if first_line_flag:
                assert elem1 > 0 and elem2 > 0, \
                    'V and E must be both non-negative values.'
            else:
                # 索引越界、自环边以及平行边的断言
                assert (0 <= elem1 < self.V and 0 <= elem2 < self.V) and \
                       (elem1 != elem2) and (not self.adj[elem1].contains(elem2)), \
                    'Vertex ({},{}) is invalid'.format(elem1, elem2)
            return elem1, elem2
        except AssertionError as e:
            print('Error in file parse stage:\n{}'.format(e))