# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2020-02-08 06:54pm


import unittest
from src.ds.graph_subject.chapter_02 import \
    adj_matrix, adj_list, adj_set, my_adj_set


class Test_Graphs(unittest.TestCase):
    def setUp(self) -> None:
        self.file_path = 'src/ds/graph_subject/data/g1.txt'
        self.graphs = [
            adj_matrix.AdjMatrix(self.file_path), adj_list.AdjList(self.file_path),
            adj_set.AdjSet(self.file_path), my_adj_set.MyAdjSet(self.file_path)
        ]

    def test_all(self):
        for graph in self.graphs:
            print('=' * 20 + ' ' + str(graph) + ' start ' + '=' * 20)

            graph.print()
            print(graph.V)
            print(graph.E)
            print(graph.has_edge(3, 4))
            print(graph.adjacent(2))
            print(graph.degree(2))

            print('=' * 20 + ' ' + str(graph) + ' end ' + '=' * 20)


if __name__ == '__main__':
    unittest.main()