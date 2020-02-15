# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2020-02-15 02:44pm


from src.ds.graph_subject.chapter_02 import my_adj_set, adj_matrix
from src.ds.graph_subject.chapter_05 import graph_bfs
import unittest


class Test_GraphBfs(unittest.TestCase):
    def setUp(self) -> None:
        graph_file_path = 'src/ds/graph_subject/data/g5.txt'
        self.test_adj_matrix = graph_bfs.GraphBfs(
            adj_matrix.AdjMatrix(graph_file_path)
        )
        self.test_adj_set = graph_bfs.GraphBfs(
            my_adj_set.MyAdjSet(graph_file_path)
        )

    def test_all(self):
        print('基于邻接矩阵的广度优先遍历：')
        print('\t先序广度优先遍历：', self.test_adj_matrix.get_bfs_order())
        print('\t后序广度优先遍历：', self.test_adj_matrix.get_bfs_order())
        print('基于邻接表的广度优先遍历：')
        print('\t先序广度优先遍历：', self.test_adj_set.get_bfs_order())
        print('\t后序广度优先遍历：', self.test_adj_set.get_bfs_order())


if __name__ == '__main__':
    unittest.main()