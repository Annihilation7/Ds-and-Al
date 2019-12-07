import unittest
from src.ds.array_queue import ArrayQueue


class Test_ArrayQueue(unittest.TestCase):
    def setUp(self) -> None:
        self.processer = ArrayQueue()

    def test_all(self):
        elems = [i for i in range(10)]

        for index, elem in enumerate(elems):
            if index != 0 and index % 3 == 0:
                self.processer.dequeue()
                self.processer.printQueue()
                continue
            self.processer.enqueue(elem)


if __name__ == '__main__':
    unittest.main()
