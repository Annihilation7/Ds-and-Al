# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2020-02-15 06:14pm


from src.ds.graph_subject.chapter_02 import my_adj_set, adj_matrix
from src.ds.graph_subject.chapter_05 import usss_path
import unittest


class Test_USSSPath(unittest.TestCase):
    def setUp(self) -> None:
        graph_file_path = 'src/ds/graph_subject/data/g5.txt'
        source = 0  # 源设为0
        self.test_adj_matrix = usss_path.USSSPath(
            adj_matrix.AdjMatrix(graph_file_path), source
        )
        self.test_adj_set = usss_path.USSSPath(
            my_adj_set.MyAdjSet(graph_file_path), source
        )

    def test_all(self):
        print('基于邻接矩阵的图：')
        print(self.test_adj_matrix.is_connected_to(6))
        print('source(0) to node(6) path: {}\nminimum_distance: {}'.format(
            self.test_adj_matrix.path(6), self.test_adj_matrix.get_distance(6)
        ))
        print('source(0) to node(5) path: {}\nminimum_distance: {}'.format(
            self.test_adj_matrix.path(5), self.test_adj_matrix.get_distance(5)
        ))
        print('=' * 20, '华丽分割线', '=' * 20)
        print('基于邻接表的图：')
        print(self.test_adj_set.is_connected_to(6))
        print('source(0) to node(6) path: {}\nminimum_distance: {}'.format(
            self.test_adj_set.path(6), self.test_adj_set.get_distance(6)
        ))
        print('source(0) to node(5) path: {}\nminimum_distance: {}'.format(
            self.test_adj_set.path(5), self.test_adj_set.get_distance(5)
        ))


if __name__ == '__main__':
    unittest.main()