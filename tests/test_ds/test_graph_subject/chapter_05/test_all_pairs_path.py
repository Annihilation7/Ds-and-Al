# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2020-02-15 04:15pm


from src.ds.graph_subject.chapter_02 import my_adj_set, adj_matrix
from src.ds.graph_subject.chapter_05 import all_pairs_path
import unittest


class Test_AllPariPath(unittest.TestCase):
    def setUp(self) -> None:
        graph_file_path = 'src/ds/graph_subject/data/g2.txt'
        self.source = 0  # 源设为0
        self.test_adj_matrix = all_pairs_path.AllPairPath(
            adj_matrix.AdjMatrix(graph_file_path),
        )  # 由于接口统一，直接用就完事了，但是注意此时时间复杂度为O(V^2)，而不是O(V+E)
        self.test_adj_set = all_pairs_path.AllPairPath(
            my_adj_set.MyAdjSet(graph_file_path),
        )

    def test_all(self):
        print('基于邻接矩阵的图：')
        print(self.test_adj_matrix.is_connected_to_source(0, 6))
        print('source(0) to node(6) path: {}'.format(
            self.test_adj_matrix.path_to_source(0, 6)
        ))
        print('source(0) to node(5) path: {}'.format(
            self.test_adj_matrix.path_to_source(0, 5)
        ))
        print('=' * 20, '华丽分割线', '=' * 20)
        print('基于邻接表的图：')
        print(self.test_adj_set.is_connected_to_source(0, 6))
        print('source(0) to node(6) path: {}'.format(
            self.test_adj_set.path_to_source(0, 6)
        ))
        print('source(0) to node(5) path: {}'.format(
            self.test_adj_set.path_to_source(0, 5)
        ))


if __name__ == '__main__':
    unittest.main()