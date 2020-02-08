# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2020-02-08 01:00pm


from src.ds.graph_subject.chapter_02.graph_base import GraphBase


class AdjMatrix(GraphBase):
    """
    图的"邻接矩阵"表示法
    空间复杂度较高，为O(V^2)，所以该图也叫稠密图。
    在表述"稀疏图"的时候有比较大的空间缺陷。
    """
    def __init__(self, filepath='src/ds/graph_subject/data/g.txt'):
        self._build_graph(filepath)

    def __str__(self):
        return 'AdjMatrix'

    def print(self):
        """打印邻接表的成员函数"""
        print('V = {}, E = {}'.format(self.V, self.E))
        for i in range(self.V):
            print_line = ' '.join(str(elem) for elem in self.adj[i])
            print(print_line)

    def V(self):
        """返回Vertex的数量"""
        return self.V

    def E(self):
        """返回Edge的数量"""
        return self.E

    def has_edge(self, v, w):
        """判断两个Vertex之间是否存在边，O(1)"""
        self._validate_vertex(v)
        self._validate_vertex(w)
        return self.adj[v][w] == 1

    def adjacent(self, v):
        """
        拿到所有与输入Vertex相邻的Vertex，O(V)
        非常重要的函数，时间复杂度是O(V)难以接受。
        """
        self._validate_vertex(v)
        return [i for i in range(self.V) if self.adj[v][i] == 1]

    def degree(self, v):
        """拿到输入Vertex的边的数量"""
        return len(self.adjacent(v))

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
                        self.adj = [[0] * self.V for _ in range(self.V)]
                        first_line_flag = False
                    else:
                        elem1, elem2 = self._valid_check_parse(
                            line, first_line_flag
                        )
                        # 注意是无向图
                        self.adj[elem1][elem2], self.adj[elem2][elem1] = 1, 1
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
                       (elem1 != elem2) and (self.adj[elem1][elem2] != 1), \
                    'Vertex ({},{}) is invalid'.format(elem1, elem2)
            return elem1, elem2
        except AssertionError as e:
            print('Error in file parse stage:\n{}'.format(e))