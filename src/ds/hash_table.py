# -*- coding: utf-8 -*-
# Email: 763366463@qq.com
# Created: 2020-02-07 05:11pm


from src.ds.avl_map import AvlMap


class HashTable:
    """
        本节哈希表的实现原理采用数组avl树的方式来实现，实际上用红黑树是最好的选择，但是
    上节实现的红黑树并没有实现删除操作，故重在理解而言，问题不大。
        哈希函数的三个主要性质：一致、高效、均匀性。
        本节实现的hash table其实就是一个简易的 dict
    """
    # upper_tolerate和lower_tolerate代表了平均每个索引处所容纳键值对个数的上界与下界
    # 有了上面两个量，我们的hash table就支持自动扩容/缩容了
    upper_tolerate = 10
    lower_tolerate = 2
    inial_capacity = 2  # 设小点，更能能看到扩容的效果。。。一般默认设为100左右好点

    def __init__(self):
        """哈希表构造函数"""
        self.m = self.inial_capacity
        self.size = 0  # 初始哈希表中没有元素
        # 初始化hash table，注意深拷贝。列表的每个元素都是一个avl树
        self.hash_table = [AvlMap() for _ in range(self.m)]

    def hash(self, key):
        """
        核心函数，拿到key的hash index
        :param key: 传入的任意的可哈希的元素
        """
        # 系统的hash函数得到的值不一定是正数，所以要转正数后再模m
        # 因为hash(-55)的结果就是-55，此时不转正直接取拿索引会出错的
        return (hash(key) & 0x7fffffff) % self.m

    def getSize(self):
        return self.size

    def add(self, key, value):
        """向哈希表中添加键、值数据对"""
        hash_idx = self.hash(key)
        if self.hash_table[hash_idx].contains(key):
            self.hash_table[hash_idx].set(key, value)
        else:
            self.hash_table[hash_idx].add(key, value)
            self.size += 1

            if self.m * self.upper_tolerate <= self.size:
                self._resize(2 * self.m)  # 扩容为原先容量的两倍

    def remove(self, key):
        """删除哈希表中的某个键，并返回其值"""
        ret = self.hash_table[self.hash(key)].remove(key)
        if ret is not None:  # 真的存在才更新self.size
            self.size -= 1

            if (self.m * self.lower_tolerate >= self.size) and \
                    (self.size >= self.inial_capacity * 2):
                # 所容为原先容量的一半，并且最小缩到self.inial_capacity
                self._resize(self.m // 2)

        return ret

    def set(self, key, value):
        """更改哈希表中已经存在的键值对其键所对应的值，不存在会报错"""
        self.hash_table[self.hash(key)].set(key, value)

    def contains(self, key):
        """查看某个键时候已经存在于哈希表中"""
        return self.hash_table[self.hash(key)].contains(key)

    def get(self, key):
        """返回某一个键所对应的值，不存在会返回None"""
        return self.hash_table[self.hash(key)].get(key)

    def print(self):
        for i in range(self.m):
            print('idx: {}'.format(i), end='---->')
            self.hash_table[i].print()
        print('Current hashtable\'s size: {}'.format(self.size))
        print('Avg occupancy: {}'.format(self.size / self.m))

    def _resize(self, new_m):
        new_has_table = [AvlMap() for _ in range(new_m)]

        old_m = self.m
        self.m = new_m
        resize_info = \
            'Capacity has been expanded' if new_m > old_m \
                else 'Capacity has been shrunk'
        print(resize_info)

        for i in range(old_m):
            for k, v in self.hash_table[i].items():
                # 注意此时计算hash_index已经是基于新hash_map的
                # 容量来计算的了，所以没毛病。
                new_has_table[self.hash(k)].add(k, v)

        self.hash_table = new_has_table  # 更新self.hash_table
