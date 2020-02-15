# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2020-02-10 01:38am


from src.ds.graph_subject.chapter_02 import my_adj_set, adj_matrix
from src.ds.graph_subject.chapter_03 import graph_dfs
import unittest


class Test_GraphDfs(unittest.TestCase):
    def setUp(self) -> None:
        self.test_adj_matrix = graph_dfs.GraphDfs(
            adj_matrix.AdjMatrix('src/ds/graph_subject/data/g2.txt')
        )  # 由于接口统一，直接用就完事了，但是注意此时时间复杂度为O(V^2)，而不是O(V+E)
        self.test_adj_set = graph_dfs.GraphDfs(
            my_adj_set.MyAdjSet('src/ds/graph_subject/data/g2.txt')
        )

    def test_all(self):
        print('基于邻接矩阵的深度优先遍历：')
        print('\t先序深度优先遍历：', self.test_adj_matrix.get_pre_order())
        print('\t后序深度优先遍历：', self.test_adj_matrix.get_post_order())
        print('基于邻接表的深度优先遍历：')
        print('\t先序深度优先遍历：', self.test_adj_set.get_pre_order())
        print('\t后序深度优先遍历：', self.test_adj_set.get_post_order())


if __name__ == '__main__':
    unittest.main()