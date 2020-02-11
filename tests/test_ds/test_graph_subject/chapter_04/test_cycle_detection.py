# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2020-02-11 09:11pm


from src.ds.graph_subject.chapter_02 import my_adj_set, adj_matrix
from src.ds.graph_subject.chapter_04 import cycle_detection
import unittest


class Test_CycleDetection(unittest.TestCase):
    def setUp(self) -> None:
        self.test_adj_matrix1 = cycle_detection.CycleDetection(
            adj_matrix.AdjMatrix('src/ds/graph_subject/data/g2.txt')
        )
        self.test_adj_matrix2 = cycle_detection.CycleDetection(
            adj_matrix.AdjMatrix('src/ds/graph_subject/data/g3.txt')
        )
        self.test_adj_set1 = cycle_detection.CycleDetection(
            my_adj_set.MyAdjSet('src/ds/graph_subject/data/g2.txt')
        )
        self.test_adj_set2 = cycle_detection.CycleDetection(
            my_adj_set.MyAdjSet('src/ds/graph_subject/data/g3.txt')
        )

    def test_all(self):
        print('基于邻接矩阵的图：')
        print(self.test_adj_matrix1.has_cycle())
        print(self.test_adj_matrix2.has_cycle())
        print('=' * 20, '华丽分割线', '=' * 20)
        print('基于邻接表的图：')
        print(self.test_adj_set1.has_cycle())
        print(self.test_adj_set2.has_cycle())


if __name__ == '__main__':
    unittest.main()