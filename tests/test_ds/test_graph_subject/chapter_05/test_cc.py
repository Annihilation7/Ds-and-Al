# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2020-02-15 04:55pm


from src.ds.graph_subject.chapter_02 import my_adj_set, adj_matrix
from src.ds.graph_subject.chapter_05 import cc
import unittest


class Test_CC(unittest.TestCase):
    def setUp(self) -> None:
        graph_file_Path = 'src/ds/graph_subject/data/g2.txt'
        self.test_adj_matrix = cc.CC(adj_matrix.AdjMatrix(graph_file_Path))
        self.test_adj_set = cc.CC(my_adj_set.MyAdjSet(graph_file_Path))

    def test_all(self):
        print('基于邻接矩阵的图：')
        print(self.test_adj_matrix.cccount)
        print(self.test_adj_matrix.is_connected(0, 6))
        print(self.test_adj_matrix.is_connected(0, 5))
        self._print_components(self.test_adj_matrix.components)
        print('=' * 20, '华丽分割线', '=' * 20)
        print('基于邻接表的图：')
        print(self.test_adj_set.cccount)
        print(self.test_adj_set.is_connected(0, 6))
        print(self.test_adj_set.is_connected(0, 5))
        self._print_components(self.test_adj_set.components)

    def _print_components(self, components):
        for i in range(len(components)):
            print(i, ':', ' '.join(map(str, components[i])))


if __name__ == '__main__':
    unittest.main()