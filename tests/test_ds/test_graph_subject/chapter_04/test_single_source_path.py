# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2020-02-12 12:47am


from src.ds.graph_subject.chapter_02 import my_adj_set, adj_matrix
from src.ds.graph_subject.chapter_04 import single_source_path
import unittest


class Test_GraphDfs(unittest.TestCase):
    def setUp(self) -> None:
        self.source = 0  # 源设为0
        self.test_adj_matrix = single_source_path.SingleSourcePath(
            adj_matrix.AdjMatrix('src/ds/graph_subject/data/g2.txt'),
            0
        )  # 由于接口统一，直接用就完事了，但是注意此时时间复杂度为O(V^2)，而不是O(V+E)
        self.test_adj_set = single_source_path.SingleSourcePath(
            my_adj_set.MyAdjSet('src/ds/graph_subject/data/g2.txt'),
            0
        )

    def test_all(self):
        print('基于邻接矩阵的图：')
        print(self.test_adj_matrix.is_connected_to(6))
        print('source(0) to node(6) path: {}'.format(
            self.test_adj_matrix.path(6)
        ))
        print('source(0) to node(5) path: {}'.format(
            self.test_adj_matrix.path(5)
        ))
        print('=' * 20, '华丽分割线', '=' * 20)
        print('基于邻接表的图：')
        print(self.test_adj_set.is_connected_to(6))
        print('source(0) to node(6) path: {}'.format(
            self.test_adj_set.path(6)
        ))
        print('source(0) to node(5) path: {}'.format(
            self.test_adj_set.path(5)
        ))


if __name__ == '__main__':
    unittest.main()