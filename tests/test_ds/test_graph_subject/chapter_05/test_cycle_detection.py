# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2020-02-15 05:11pm


from src.ds.graph_subject.chapter_02 import my_adj_set, adj_matrix
from src.ds.graph_subject.chapter_05 import cycle_detection
import unittest


class Test_CycleDetection(unittest.TestCase):
    def setUp(self) -> None:
        graph_file_path1 = 'src/ds/graph_subject/data/g2.txt'
        graph_file_path2 = 'src/ds/graph_subject/data/g3.txt'
        self.test_adj_matrix1 = cycle_detection.CycleDetection(
            adj_matrix.AdjMatrix(graph_file_path1)
        )
        self.test_adj_matrix2 = cycle_detection.CycleDetection(
            adj_matrix.AdjMatrix(graph_file_path2)
        )
        self.test_adj_set1 = cycle_detection.CycleDetection(
            my_adj_set.MyAdjSet(graph_file_path1)
        )
        self.test_adj_set2 = cycle_detection.CycleDetection(
            my_adj_set.MyAdjSet(graph_file_path2)
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