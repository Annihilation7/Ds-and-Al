# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2020-02-11 09:32pm


from src.ds.graph_subject.chapter_04 import cc
from src.ds.graph_subject.chapter_04 import cycle_detection


class IsTree:
    def __init__(self, graph):
        """
        判断传入的图是否能用树来表示。
        能表示成树的两个条件是：1、一个连通分量 2、无环 要同时满足。
        基于以前实现的cc类和cycle_detection类，实现起来非常的方便。
        :param graph: 传入的图
        """
        self.graph = graph
        self.cc_detector = cc.CC(self.graph)
        self.cycle_detector = cycle_detection.CycleDetection(self.graph)

    def is_tree(self):
        """判断传入的图是否能表示成一棵树"""
        return self.cc_detector.cccount == 1 and \
               not self.cycle_detector.has_cycle()