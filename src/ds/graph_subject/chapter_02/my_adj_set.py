# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2020-02-09 01:16am


from src.ds.graph_subject.chapter_02.graph_base import GraphBase


class MyAdjSet(GraphBase):
    """
    图的"邻接表(HashSet)"表示法。建图空间复杂度为O(Elog(V))，时间复杂度为O(E*V)
    这里和bobo老师不一样了哈，以后我用hash set作为邻接表的底层数据结构了，并非红黑树。
    时间复杂度更低，从logV变成常数时间了。
    """
    def __init__(self, filepath):
        self._build_graph(filepath)

    def __str__(self):
        return 'MyAdjSet'

    def print(self):
        """打印邻接表的成员函数"""
        print('V = {}, E = {}'.format(self.V, self.E))
        for i in range(self.V):
            print_line = ' '.join(str(elem) for elem in self.adj[i])
            print('{} :'.format(i), print_line)

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
        return w in self.adj[v]

    def adjacent(self, v):
        """拿到所有与输入Vertex相邻的Vertex，返回对应的hash set，O(1)"""
        self._validate_vertex(v)
        return self.adj[v]

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
                        # 邻接表其实就是数组套链表的结构
                        self.adj = [set() for _ in range(self.V)]
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
                       (elem1 != elem2) and (not elem2 in self.adj[elem1]), \
                    'Vertex ({},{}) is invalid'.format(elem1, elem2)
            return elem1, elem2
        except AssertionError as e:
            print('Error in file parse stage:\n{}'.format(e))