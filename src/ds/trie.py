# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-12-21 07:59pm


class Node:
    def __init__(self, isword=False):
        self.isword = isword
        # key -> node 结构
        self.next = {}


class Trie:
    def __init__(self):
        self.root = Node()
        self.size = 0

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def add(self, astring):
        """向trie中增加一个单词astring"""
        cur_node = self.root
        for elem in astring:
            is_exist = cur_node.next.get(elem, None)
            if is_exist is None:
                cur_node.next[elem] = Node()
            cur_node = cur_node.next[elem]
        if not cur_node.isword:
            cur_node.isword = True
            self.size += 1

    def add_re(self, astring):
        self._add_re(self.root, astring)

    def contains(self, astring):
        """查询trie中是否包含astring"""
        cur_node = self.root
        for elem in astring:
            is_exist = cur_node.next.get(elem, None)
            if is_exist is None:
                return False
            cur_node = cur_node.next[elem]
        return cur_node.isword  # 最后别忘了isword只有是True才表明真正的存在

    def contains_re(self, astring):
        return self._contains_re(self.root, astring)

    def is_prefix(self, prefix):
        """
        查看trie中是否包含前缀prefix，最后的判断条件要比contains简单，因为不需要
        确定单词是否一定存在
        """
        cur_node = self.root
        for elem in prefix:
            is_exist = cur_node.next.get(elem, None)
            if is_exist is None:
                return False
            cur_node = cur_node.next[elem]
        return True

    def is_prefix_re(self, prefix):
        return self._is_prefix_re(self.root, prefix)

    def print(self):
        self._print(self.root)
        print('Size: {}'.format(self.getSize()))

    # private
    def _print(self, node):
        """打印以node为根结点的trie"""
        if len(node.next.keys()) == 0:
            print('None')
            return
        for key in node.next.keys():
            print(key, end='->')
            self._print(node.next[key])

    def _add_re(self, node, astring):
        """向以node为根结点的trie添加字符串astring，递归调用函数"""
        if len(astring) == 0:
            if not node.isword:
                node.isword = True
                self.size += 1
            return

        is_exist = node.next.get(astring[0], None)
        if is_exist is None:
            node.next[astring[0]] = Node()
        self._add_re(node.next[astring[0]], astring[1:])

    def _contains_re(self, node, astring):
        """查询node为根结点的trie中是否包含字符串astring"""
        if len(astring) == 0:
            return node.isword  # 一样的，最后也要检查isword是否真的是True

        is_exist = node.next.get(astring[0], None)
        if is_exist is None:
            return False
        return self._contains_re(node.next[astring[0]], astring[1:])

    def _is_prefix_re(self, node, prefix):
        '''判断以node为根结点的trie中是否包含前缀prefix'''
        if len(prefix) == 0:
            return True

        is_exist = node.next.get(prefix[0], None)
        if is_exist is None:
            return False
        return self._is_prefix_re(node.next[prefix[0]], prefix[1:])
