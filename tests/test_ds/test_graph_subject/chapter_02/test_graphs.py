# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2020-02-08 06:54pm


import unittest
from src.ds.graph_subject.chapter_02 import adj_matrix, adj_list, adj_set


class Test_Graphs(unittest.TestCase):
    def setUp(self) -> None:
        self.graphs = [
            adj_matrix.AdjMatrix(), adj_list.AdjList(), adj_set.AdjSet()
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