# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2019-01-18 04:10pm


import abc


class UnionFindBase(metaclass=abc.ABCMeta):
    def __init__(self, size):
        self.size = size

    @abc.abstractmethod
    def getSize(self):
        pass

    @abc.abstractmethod
    def find(self, p):
        """找到索引p所属的集合"""
        pass

    @abc.abstractmethod
    def isConnected(self, p, q):
        """查看索引p和索引q是否属于同一个集合"""
        pass

    @abc.abstractmethod
    def union(self, p, q):
        """将索引p和索引q所在的两个集合合并"""
        pass


class UnionFind1(UnionFindBase):
    def __init__(self, size):
        """查找快，union慢"""
        super(UnionFind1, self).__init__(size)
        self.size = size
        self.id = [i for i in range(self.size)]  # 刚开始各自成派

    def __repr__(self):
        return 'UnionFind1'

    def getSize(self):
        return self.size

    def find(self, p):
        assert 0 <= p < self.size, 'Invalid index.'
        return self.id[p]

    def isConnected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)

        if p_root == q_root:
            return

        for i in range(self.size):
            if self.id[i] == q_root:  # if self.id[i] == p_root
                self.id[i] = p_root  # self.id[i] = q_root


class UnionFind2(UnionFindBase):
    def __init__(self, size):
        super(UnionFind2, self).__init__(size)
        self.parent = [i for i in range(self.size)]

    def __repr__(self):
        return 'UnionFind2'

    def getSize(self):
        return self.size

    def find(self, p):
        """找跟节点index，O(h)"""
        assert 0 <= p < self.size, 'Invalid index.'
        while p != self.parent[p]:
            p = self.parent[p]
        return p

    def isConnected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        """O(h)"""
        p_root = self.find(p)
        q_root = self.find(q)

        if p_root == q_root:
            return

        self.parent[p_root] = q_root  # self.parent[q_root] = p_root 也行


class UnionFind3(UnionFindBase):
    def __init__(self, size):
        super(UnionFind3, self).__init__(size)
        self.parent = [i for i in range(self.size)]
        self.sz = [1 for _ in range(self.size)]

    def __repr__(self):
        return 'UnionFind3'

    def getSize(self):
        return self.size

    def find(self, p):
        """找跟节点index，O(h)"""
        assert 0 <= p < self.size, 'Invalid index.'
        while p != self.parent[p]:
            p = self.parent[p]
        return p

    def isConnected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        """O(h)"""
        p_root = self.find(p)
        q_root = self.find(q)

        if p_root == q_root:
            return

        if self.sz[p_root] < self.sz[q_root]:
            self.parent[p_root] = q_root
            self.sz[q_root] += self.sz[p_root]
        else:
            self.parent[q_root] = p_root
            self.sz[p_root] += self.sz[q_root]


class UnionFind4(UnionFindBase):
    def __init__(self, size):
        """基于rank的优化"""
        super(UnionFind4, self).__init__(size)
        self.parent = [i for i in range(self.size)]
        self.rank = [1 for _ in range(self.size)]

    def __repr__(self):
        return 'UnionFind4'

    def getSize(self):
        return self.size

    def find(self, p):
        """找跟节点index，O(h)"""
        assert 0 <= p < self.size, 'Invalid index.'
        while p != self.parent[p]:
            p = self.parent[p]
        return p

    def isConnected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        """O(h)"""
        p_root = self.find(p)
        q_root = self.find(q)

        if p_root == q_root:
            return

        if self.rank[p_root] < self.rank[q_root]:
            self.parent[p_root] = q_root
        elif self.rank[q_root] < self.rank[p_root]:
            self.parent[q_root] = p_root
        else:  # 这个时候随意了，只是需要维护一下self.rank
            self.parent[p_root] = q_root
            self.rank[q_root] += 1


class UnionFind5(UnionFindBase):
    def __init__(self, size):
        """基于rank与路径压缩的优化，非常经典的结构，一定要会"""
        super(UnionFind5, self).__init__(size)
        self.parent = [i for i in range(self.size)]
        self.rank = [1 for _ in range(self.size)]

    def __repr__(self):
        return 'UnionFind5'

    def getSize(self):
        return self.size

    def find(self, p):
        """找跟节点index，O(h)"""
        assert 0 <= p < self.size, 'Invalid index.'
        while p != self.parent[p]:
            # 路径压缩就这么一行代码，也很好理解
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def isConnected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        """O(h)"""
        p_root = self.find(p)
        q_root = self.find(q)

        if p_root == q_root:
            return

        if self.rank[p_root] < self.rank[q_root]:
            self.parent[p_root] = q_root
        elif self.rank[q_root] < self.rank[p_root]:
            self.parent[q_root] = p_root
        else:  # 这个时候随意了，只是需要维护一下self.rank
            self.parent[p_root] = q_root
            self.rank[q_root] += 1


class UnionFind6(UnionFindBase):
    def __init__(self, size):
        """更狠的路径压缩"""
        super(UnionFind6, self).__init__(size)
        self.parent = [i for i in range(self.size)]
        self.rank = [1 for _ in range(self.size)]

    def __repr__(self):
        return 'UnionFind6'

    def getSize(self):
        return self.size

    def find(self, p):
        """找跟节点index，O(h)"""
        assert 0 <= p < self.size, 'Invalid index.'
        if p != self.parent[p]:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def isConnected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        """O(h)"""
        p_root = self.find(p)
        q_root = self.find(q)

        if p_root == q_root:
            return

        if self.rank[p_root] < self.rank[q_root]:
            self.parent[p_root] = q_root
        elif self.rank[q_root] < self.rank[p_root]:
            self.parent[q_root] = p_root
        else:  # 这个时候随意了，只是需要维护一下self.rank
            self.parent[p_root] = q_root
            self.rank[q_root] += 1

