# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2020-02-12 12:35am


from src.ds.graph_subject.chapter_04 import single_source_path


class AllPairPath:
    def __init__(self, graph):
        """
        图多源路径的构造函数，就是封装一下单源的，很简单
        :param graph: 传入的图
        """
        self.graph = graph
        self.total_paths = [[] for _ in range(self.graph.V)]

        # 遍历每个节点，都作为源就完事了
        for node_idx in range(self.graph.V):
            self.total_paths[node_idx] = single_source_path.SingleSourcePath(
                self.graph, node_idx
            )

    def is_connected_to_source(self, s, v):
        """
        判断节点w是否在源s的单源路径中
        :param s: 传入的源
        :param v: 传入的另一个节点
        """
        self.graph.validate_vertex(s)
        return self.total_paths[s].is_connected_to(v)

    def path_to_source(self, s, v):
        """
        求从源s到节点v的一条单源路径
        :param s: 传入的源
        :param v: 传入的另一个节点
        """
        self.graph.validate_vertex(s)
        return self.total_paths[s].path(v)