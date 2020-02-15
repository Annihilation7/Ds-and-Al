# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2020-02-15 04:11pm


from src.ds.graph_subject.chapter_02 import my_adj_set, adj_matrix
from src.ds.graph_subject.chapter_05 import path
import unittest


class Test_Path(unittest.TestCase):
    def setUp(self) -> None:
        graph_file_path = 'src/ds/graph_subject/data/g2.txt'
        self.s_t = [(0, 6), (0, 1), (0, 5)]
        self.adj_matrix_processers = []
        self.adj_set_processers = []
        for st_item in self.s_t:
            self.adj_matrix_processers.append(
                path.Path(adj_matrix.AdjMatrix(graph_file_path), *st_item),
            )
            self.adj_set_processers.append(
                path.Path(my_adj_set.MyAdjSet(graph_file_path), *st_item)
            )

    def test_all(self):
        print('基于邻接矩阵的图：')
        for i in range(len(self.s_t)):
            print('source({}) to node({}) path: {}'.format(
                self.s_t[i][0], self.s_t[i][1],
                self.adj_matrix_processers[i].path
            ))
        print('=' * 20, '华丽分割线', '=' * 20)
        print('基于邻接表的图：')
        for i in range(len(self.s_t)):
            print('source({}) to node({}) path: {}'.format(
                self.s_t[i][0], self.s_t[i][1],
                self.adj_set_processers[i].path
            ))


if __name__ == '__main__':
    unittest.main()