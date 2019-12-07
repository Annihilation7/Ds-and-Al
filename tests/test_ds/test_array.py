import unittest
from src.ds.array import Array


class Test_Array(unittest.TestCase):
    def setUp(self) -> None:
        self.processer = Array()

    def test_all(self):
        print(self.processer.getSize())
        print(self.processer.isEmpty())

        # 插入[3, 4, 5]
        for elem in [3, 4, 5]:
            self.processer.add(0, elem)
        self.processer.printArray()
        # get
        print(self.processer.get(1))
        # set
        self.processer.set(2, 'hello')
        self.processer.printArray()
        # contains
        print(self.processer.contains(5))
        # find
        print(self.processer.find('hello'))
        # remove
        self.processer.remove(1)
        self.processer.printArray()
        # removeElement
        self.processer.removeElement('hello')
        self.processer.printArray()
        # expand
        for i in range(10):
            self.processer.add(0, i)
        self.processer.printArray()


if __name__ == '__main__':
    unittest.main()