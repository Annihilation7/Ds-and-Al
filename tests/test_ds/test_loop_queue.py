import unittest
from src.ds.loop_queue import LoopQueue


class Test_LoopQueue(unittest.TestCase):
    def setUp(self) -> None:
        self.processer = LoopQueue()

    def test_all(self):
        elems = [i for i in range(40)]
        for elem in elems:
            self.processer.enqueue(elem)
        self.processer.printLoopQueue()
        for i in range(37):
            self.processer.dequeue()
        self.processer.printLoopQueue()


if __name__ == '__main__':
    unittest.main()