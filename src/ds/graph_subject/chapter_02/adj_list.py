# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2020-02-08 05:06pm


from src.ds.linked_list import LinkedList
from src.ds.graph_subject.chapter_02.graph_base import GraphBase


class AdjList(GraphBase):
    """
    图的"邻接表(LinkedList)"表示法。键图空间复杂度为O(V+E)，时间复杂度为O(E*V)
    由于has_edge以及adjacent的时间复杂度不令人满意，因此其改进措施就是将链表换成
    哈希表或者红黑树就可以了。
    """
    def __init__(self, filepath='src/ds/graph_subject/data/g.txt'):
        self._build_graph(filepath)

    def __str__(self):
        return 'AdjList'

    def print(self):
        """打印邻接表的成员函数"""
        print('V = {}, E = {}'.format(self.V, self.E))
        for i in range(self.V):
            print('{} :'.format(i), self.adj[i].print_in_adj_list())

    def V(self):
        """返回Vertex的数量"""
        return self.V

    def E(self):
        """返回Edge的数量"""
        return self.E

    def has_edge(self, v, w):
        """判断两个Vertex之间是否存在边，O(degree(v))"""
        self._validate_vertex(v)
        self._validate_vertex(w)
        return self.adj[v].contains(w)

    def adjacent(self, v):
        """拿到所有与输入Vertex相邻的Vertex，直接返回所对应链表的头节点，O(degree(v))"""
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
                        self.adj = [LinkedList() for _ in range(self.V)]
                        first_line_flag = False
                    else:
                        elem1, elem2 = self._valid_check_parse(
                            line, first_line_flag
                        )
                        # 注意是无向图
                        self.adj[elem1].addFirst(elem2)  # O(1)
                        self.adj[elem2].addFirst(elem1)
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