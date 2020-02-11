# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2020-02-11 09:36pm


from src.ds.graph_subject.chapter_02 import my_adj_set, adj_matrix
from src.ds.graph_subject.chapter_04 import bipartition_detection
import unittest


class Test_BiPartitionDetection(unittest.TestCase):
    def setUp(self) -> None:
        self.test_adj_matrix1 = bipartition_detection.BiPartitionDetection(
            adj_matrix.AdjMatrix('src/ds/graph_subject/data/g3.txt')
        )
        self.test_adj_matrix2 = bipartition_detection.BiPartitionDetection(
            adj_matrix.AdjMatrix('src/ds/graph_subject/data/g4.txt')
        )
        self.test_adj_set1 = bipartition_detection.BiPartitionDetection(
            my_adj_set.MyAdjSet('src/ds/graph_subject/data/g3.txt')
        )
        self.test_adj_set2 = bipartition_detection.BiPartitionDetection(
            my_adj_set.MyAdjSet('src/ds/graph_subject/data/g4.txt')
        )

    def test_all(self):
        # 由于5是孤立点，自成连通分量，所以这里返回的应该都是False
        print('基于邻接矩阵的图：')
        print(self.test_adj_matrix1.is_bipartite())
        print(self.test_adj_matrix1.get_patrition_vertexes())
        print(self.test_adj_matrix2.is_bipartite())
        print(self.test_adj_matrix2.get_patrition_vertexes())
        print('=' * 20, '华丽分割线', '=' * 20)
        print('基于邻接表的图：')
        print(self.test_adj_set1.is_bipartite())
        print(self.test_adj_set1.get_patrition_vertexes())
        print(self.test_adj_set2.is_bipartite())
        print(self.test_adj_set2.get_patrition_vertexes())


if __name__ == '__main__':
    unittest.main()